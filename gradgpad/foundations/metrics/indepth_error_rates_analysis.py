import itertools
import numpy as np

from typing import Dict, Any

from dataclasses import dataclass

from gradgpad.foundations.metrics.apcer_fixing_bpcer import apcer_fixing_bpcer
from gradgpad.foundations.metrics.bpcer import bpcer
from gradgpad.foundations.metrics.bpcer_fixing_apcer import bpcer_fixing_apcer


@dataclass
class InDepthErrorRatesResult:
    acer: float
    bpcer: float
    max_apcer_label: str
    apcer_per_label: Dict[str, float]
    acer_per_label: Dict[str, float]
    num_samples_per_label: Dict[str, int]
    percentage_per_label: Dict[str, float]
    wacer: float
    weighted_apcer_per_label: Dict[str, float]

    def __init__(
        self,
        bpcer_value: float,
        relative_working_points: Dict,
        max_apcer_value: float,
        max_apcer_label: str,
        apcer_per_label: Dict[str, float],
        apcer_per_label_fixing_bpcer: Dict[str, Any],
        num_samples_per_label: Dict[str, int],
    ):

        self.acer = (max_apcer_value + bpcer_value) / 2
        self.bpcer = bpcer_value
        self.relative_working_points = relative_working_points
        self.max_apcer_label = max_apcer_label
        self.apcer_per_label = apcer_per_label
        self.apcer_per_label_fixing_bpcer = apcer_per_label_fixing_bpcer
        self.acer_per_label = {}

        for label, apcer in apcer_per_label.items():
            self.acer_per_label[label] = (apcer + bpcer_value) / 2
        self.num_samples_per_label = num_samples_per_label
        total_samples = sum(
            [num_samples for num_samples in self.num_samples_per_label.values()]
        )
        self.percentage_per_label = {}
        for label, num_samples in self.num_samples_per_label.items():
            self.percentage_per_label[label] = (
                100.0 * float(num_samples) / float(total_samples)
            )

        self.weighted_apcer_per_label = {}
        for label, apcer in self.apcer_per_label.items():
            w = self.percentage_per_label[label]
            self.weighted_apcer_per_label[label] = apcer * (w / 100.0)

        weighted_sum = sum(list(self.weighted_apcer_per_label.values()))

        self.wacer = (weighted_sum + bpcer_value) / 2

    def to_dict(self, label_modificator="label"):
        return {
            "acer": self.acer,
            "bpcer": self.bpcer,
            "relative_working_points": self.relative_working_points,
            f"max_apcer_{label_modificator}": self.max_apcer_label,
            f"apcer_per_{label_modificator}": self.apcer_per_label,
            f"apcer_per_{label_modificator}_fixing_bpcer": self.apcer_per_label_fixing_bpcer,
            f"acer_per_{label_modificator}": self.acer_per_label,
            f"num_samples_per_{label_modificator}": self.num_samples_per_label,
            f"percentage_per_{label_modificator}": self.percentage_per_label,
            "wacer": self.wacer,
            f"weighted_apcer_per_{label_modificator}": self.weighted_apcer_per_label,
        }


def indepth_error_rates_analysis(
    scores,
    labels,
    working_point_thresholds,
    meta_label_info,
    bpcer_fixing_working_points=None,
    apcer_fixing_working_points=None,
) -> Dict[str, InDepthErrorRatesResult]:
    """
    Computes the Attack Classification Error Rate.

    Parameters
    ----------
    scores: np array
        It holds the score information for all samples (genuine and impostor).
        It is expected that impostor (negative) scores are, at least by design, greater than genuine (positive) scores.
    labels: np array
        It holds the labels (int). It is assumed that impostor_labels != 0 and genuine labels == 0
    working_point_thresholds
        Dictionary with thresholds for different working points.
        e.g Equal Error Rate threshold at dev subset working_point_thresholds = {"eer": 0.5}
        Every impostor sample that falls bellow the threshold is considered a
        false-accept (FA). Genuine samples above the threshold are considered a false-rejection (FR).
    meta_label_info
        Dict with the information to aggregate labels. e.g {"print": [1, 2, 3], "replay": [4, 5, 6], "mask": [7, 8, 9]}
    bpcer_fixing_working_points
        List with BPCER fixing working points. In order to calculate APCER @ BPCER X %
    apcer_fixing_working_points
        List with APCER fixing working points. In order to calculate BPCER @ APCER X %
    Returns
    -------
        Dict[working_point: str, InDepthErrorRatesResult]
    """

    indepth_error_rate_results: Dict[str, InDepthErrorRatesResult] = {}
    for working_point, threshold in working_point_thresholds.items():
        bpcer_value = 100.0 * bpcer(scores, labels, threshold)
        max_apcer_label, max_apcer_value, apcer_per_label, num_samples_per_label, apcer_per_label_fixing_bpcer = apcer_analysis(
            scores,
            labels,
            threshold,
            meta_label_info,
            bpcer_fixing_working_points,
            apcer_fixing_working_points,
        )

        relative_working_points = get_relative_working_points(
            scores,
            labels,
            bpcer_fixing_working_points,
            apcer_fixing_working_points,
            meta_label_info,
        )

        indepth_error_rate_results[working_point] = InDepthErrorRatesResult(
            bpcer_value=bpcer_value,
            relative_working_points=relative_working_points,
            max_apcer_value=max_apcer_value,
            max_apcer_label=max_apcer_label,
            apcer_per_label=apcer_per_label,
            apcer_per_label_fixing_bpcer=apcer_per_label_fixing_bpcer,
            num_samples_per_label=num_samples_per_label,
        )

    return indepth_error_rate_results


def group_labels(labels, meta_label_info):
    grouped_labels = np.copy(labels)
    for i, values in enumerate(meta_label_info.values()):
        for value in values:
            grouped_labels[grouped_labels == value] = 100 + i + 1

    grouped_labels = grouped_labels - 100
    grouped_labels[grouped_labels == -100] = 0
    return grouped_labels


def get_relative_working_points(
    scores,
    labels,
    bpcer_fixing_working_points,
    apcer_fixing_working_points,
    meta_label_info,
):

    grouped_labels = group_labels(labels, meta_label_info)

    relative_working_points = {}
    if bpcer_fixing_working_points:
        relative_working_points["apcer"] = {}
        for bpcer_wp in bpcer_fixing_working_points:
            key = f"bpcer_{round(bpcer_wp * 100.0)}"
            relative_working_points["apcer"][key] = 100.0 * apcer_fixing_bpcer(
                scores, grouped_labels, bpcer_wp
            )

    if apcer_fixing_working_points:
        relative_working_points["bpcer"] = {}
        for apcer_wp in apcer_fixing_working_points:
            key = f"apcer_{round(apcer_wp * 100.0)}"
            relative_working_points["bpcer"][key] = 100.0 * bpcer_fixing_apcer(
                scores, grouped_labels, apcer_wp
            )
    return relative_working_points


def apcer_analysis(
    scores,
    labels,
    th_eer_dev,
    meta_label_info,
    bpcer_fixing_working_points=None,
    apcer_fixing_working_points=None,
):
    if not isinstance(scores, np.ndarray) or not isinstance(scores, np.ndarray):
        raise TypeError(
            "Scores [{}] and labels [{}] must be numpy arrays.".format(
                type(scores), type(labels)
            )
        )

    scores = scores.ravel()
    labels = labels.ravel()

    assert len(scores) == len(labels)

    impostor_labels = labels[labels != 0]
    impostor_pais = np.unique(impostor_labels).tolist()

    labels_from_meta = list(itertools.chain(*[v for _, v in meta_label_info.items()]))
    if not all(elem in labels_from_meta for elem in impostor_pais):
        raise ValueError(
            f"meta_label_info is not complete. "
            f"Impostor PAIs are {impostor_pais} and meta_labels_info is {meta_label_info}"
        )

    num_samples_per_label = {}
    apcer_per_label = {}
    if bpcer_fixing_working_points:
        apcer_per_label_fixing_bpcer = {}
    else:
        apcer_per_label_fixing_bpcer = None
    for reference, pais in meta_label_info.items():
        pai_scores = [scores[labels == pai] for pai in pais]
        pai_scores = np.concatenate(pai_scores)
        if pai_scores.size > 0:
            # APCER
            pai_apcer = 100 * (
                pai_scores[pai_scores < th_eer_dev].size / pai_scores.size
            )
            apcer_per_label[reference] = pai_apcer

            # APCER @ BPCER
            if bpcer_fixing_working_points:
                apcer_per_label_fixing_bpcer[reference] = {}
                for wp in bpcer_fixing_working_points:
                    genuines_scores = scores[labels == 0]
                    aggregate_scores = np.concatenate([genuines_scores, pai_scores])
                    aggregate_labels = np.array(
                        [0] * len(genuines_scores) + [1] * len(pai_scores)
                    )
                    key = f"apcer_fixing_bpcer{round(wp * 100.0)}"
                    apcer_per_label_fixing_bpcer[reference][key] = (
                        100.0
                        * apcer_fixing_bpcer(aggregate_scores, aggregate_labels, wp)
                    )

        num_samples_per_label[reference] = pai_scores.size

    max_apcer_label = max(apcer_per_label, key=apcer_per_label.get)
    max_apcer_value = apcer_per_label[max_apcer_label]

    return (
        max_apcer_label,
        max_apcer_value,
        apcer_per_label,
        num_samples_per_label,
        apcer_per_label_fixing_bpcer,
    )
