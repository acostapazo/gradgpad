import os

from gradgpad.tools.visualization.histogram.split_by_level_mode import SplitByLabelMode
from gradgpad.foundations.annotations.scenario import ScenarioColor
from gradgpad.foundations.metrics.metrics import Metrics
from gradgpad.foundations.scores.approach import Approach
from gradgpad.foundations.scores.protocol import Protocol
from gradgpad.foundations.scores.scores_provider import ScoresProvider
from gradgpad.foundations.scores.subset import Subset
from gradgpad.tools.evaluation.plots.det_curve import det_curve
from gradgpad.tools.visualization.histogram.histogram import Histogram


def get_filename(
    output_path_hists_and_curves: str,
    subset: str,
    normalize_hist: bool,
    suffix: str = "",
):
    if normalize_hist:
        output_hist_filename = (
            f"{output_path_hists_and_curves}/{subset}_hist_norm{suffix}.png"
        )
    else:
        output_hist_filename = (
            f"{output_path_hists_and_curves}/{subset}_hist{suffix}.png"
        )
    return output_hist_filename


def calculate_hists_and_curves(output_path: str, only_grandtest: bool = False):
    print("> Protocols | Calculating Hists and Curves...")

    output_path_hists_and_curves = f"{output_path}/hists_and_curves"
    os.makedirs(output_path_hists_and_curves, exist_ok=True)

    approach_protocols_subset_scores = {
        "Quality SVM RBF": ScoresProvider.all(Approach.QUALITY_RBF),
        # "Quality SVM LINEAR": ScoresProvider.all(Approach.QUALITY_LINEAR),
        "Auxiliary": ScoresProvider.all(Approach.AUXILIARY),
    }
    for approach, protocols_subset_scores in approach_protocols_subset_scores.items():

        protocol_metrics = {}
        for protocol_name, subset_scores in protocols_subset_scores.items():
            if only_grandtest and protocol_name != Protocol.GRANDTEST.value:
                continue
            protocol_metrics[protocol_name] = Metrics(
                devel_scores=subset_scores.get("devel"),
                test_scores=subset_scores.get("test"),
            )

        for protocol_name, subset_scores in protocols_subset_scores.items():
            if only_grandtest and protocol_name != Protocol.GRANDTEST.value:
                continue
            approach_name = approach.replace(" ", "_").lower()
            output_path_hists_and_curves = (
                f"{output_path}/hists_and_curves/{approach_name}/{protocol_name}"
            )
            os.makedirs(output_path_hists_and_curves, exist_ok=True)

            metrics = protocol_metrics.get(protocol_name)
            eer_th = metrics.get_eer_th(Subset.DEVEL)

            for subset, scores in subset_scores.items():

                data = {
                    "scores": scores.get_numpy_scores(),
                    "labels": scores.get_numpy_labels(),
                }

                output_det_filename = f"{output_path_hists_and_curves}/{subset}_det.png"
                det_curve(data, output_det_filename)

                for normalize_hist in [True, False]:
                    output_hist_filename = get_filename(
                        output_path_hists_and_curves, subset, normalize_hist
                    )

                    histogram = Histogram(
                        genuine_label=0,
                        plot_vertical_line_on_value=eer_th,
                        legend_vertical_line="EER @ Devel",
                        normalize=normalize_hist,
                    )
                    histogram.save(output_hist_filename, scores)

                if protocol_name == Protocol.GRANDTEST.value:
                    calculate_hists_and_curves_pai_types(
                        output_path_hists_and_curves, subset, scores, eer_th
                    )


def calculate_hists_and_curves_pai_types(
    output_path_hists_and_curves, subset, scores, eer_th
):
    output_det_filename = f"{output_path_hists_and_curves}/{subset}_det_detail.png"

    data = {
        "scores": scores.get_numpy_scores(),
        "labels": scores.get_numpy_labels_by_scenario(),
    }

    det_curve(
        data,
        output_det_filename,
        subtypes={1: "PAI Type I", 2: "PAI Type II", 3: "PAI Type III", 0: "All"},
        colors={
            1: ScenarioColor.PAS_TYPE_I.value,
            2: ScenarioColor.PAS_TYPE_II.value,
            3: ScenarioColor.PAS_TYPE_III.value,
            0: "b",
        },
    )

    for normalize_hist in [True, False]:
        output_hist_filename = get_filename(
            output_path_hists_and_curves, subset, normalize_hist, "_detail"
        )

        histogram = Histogram(
            plot_vertical_line_on_value=eer_th,
            legend_vertical_line="EER @ Devel",
            normalize=normalize_hist,
            split_by_label_mode=SplitByLabelMode.PAS,
        )
        histogram.save(output_hist_filename, scores)
