import numpy as np

from gradgpad.foundations.metrics.eer import eer
from gradgpad.foundations.metrics.frr import frr
from gradgpad.foundations.metrics.hter import hter
from gradgpad.foundations.metrics.indepth_error_rates_analysis import (
    indepth_error_rates_analysis,
)
from gradgpad.foundations.annotations.grained_pai_mode import GrainedPaiMode
from gradgpad.reproducible_research import Scores, List
from gradgpad.foundations.scores.subset import Subset


def meta_label_info_provider(fine_grained_pais: bool = True):
    if fine_grained_pais:
        meta_label_info = {
            "print_low_quality": [1],
            "print_medium_quality": [2],
            "print_high_quality": [3],
            "replay_low_quality": [4],
            "replay_medium_quality": [5],
            "replay_high_quality": [6],
            "mask_paper": [7],
            "mask_rigid": [8],
            "mask_silicone": [9],
            "makeup_cosmetic": [10],
            "makeup_impersonation": [11],
            "makeup_obfuscation": [12],
            "partial_funny_eyes": [13],
            "partial_periocular": [14],
            "partial_paper_glasses": [15],
            "partial_upper_half": [16],
            "partial_lower_half": [17],
        }
    else:
        meta_label_info = {
            "print": [1, 2, 3],
            "replay": [4, 5, 6],
            "mask": [7, 8, 9],
            "makeup": [10, 11, 12],
            "partial": [13, 14, 15, 16, 17],
        }

    return meta_label_info


class Metrics:
    def __init__(self, devel_scores: Scores, test_scores: Scores):
        self.devel_scores = devel_scores
        self.test_scores = test_scores

    def get_eer(self, subset: Subset):
        scores = self.devel_scores if subset == Subset.DEVEL else self.test_scores
        eer_value, _ = eer(scores.get_numpy_scores(), scores.get_numpy_labels())
        return eer_value

    def get_eer_th(self, subset: Subset):
        scores = self.devel_scores if subset == Subset.DEVEL else self.test_scores
        _, eer_th = eer(scores.get_numpy_scores(), scores.get_numpy_labels())
        return eer_th

    def get_frr_th(self, subset: Subset, far_op: float):
        scores = self.devel_scores if subset == Subset.DEVEL else self.test_scores
        _, frr_th = frr(scores.get_numpy_scores(), scores.get_numpy_labels(), far_op)
        return frr_th

    def get_far_th(self, subset: Subset, frr_op: float):
        scores = self.devel_scores if subset == Subset.DEVEL else self.test_scores
        _, far_th = frr(scores.get_numpy_scores(), scores.get_numpy_labels(), frr_op)
        return far_th

    def _transform_labels(self, labels, meta_label_info):
        if "print" in meta_label_info.keys():
            label_correspondences = {
                "genuine": 0,
                "print": 1,
                "replay": 2,
                "mask": 3,
                "makeup": 4,
                "partial": 5,
            }
            meta_labels = []
            for label in labels:
                if label == 0:
                    meta_labels.append("genuine")
                for meta_label, set_labels in meta_label_info.items():
                    if label in set_labels:
                        meta_labels.append(meta_label)

            labels = [
                label_correspondences.get(meta_label) for meta_label in meta_labels
            ]
            labels = np.array(labels)
        return labels

    def get_indepth_analysis(
        self,
        bpcer_fixing_working_points: List[float],
        apcer_fixing_working_points: List[float],
        selected_grained_pais: List = GrainedPaiMode.options(),
    ):
        analysis = {}

        scores_devel = self.devel_scores.get_numpy_scores()
        labels_devel = self.devel_scores.get_numpy_fine_grained_pai_labels()

        scores_test = self.test_scores.get_numpy_scores()
        labels_test = self.test_scores.get_numpy_fine_grained_pai_labels()

        for selected_grained_pai in selected_grained_pais:

            if selected_grained_pai == GrainedPaiMode.COARSE:
                labels_devel = self._transform_labels(
                    labels_devel, meta_label_info_provider(fine_grained_pais=False)
                )
                labels_test = self._transform_labels(
                    labels_test, meta_label_info_provider(fine_grained_pais=False)
                )

            _, eer_th = eer(scores_devel, labels_devel)
            _, eer_th_test = eer(scores_test, labels_test)

            hter_value = hter(scores_test, labels_test, eer_th)

            fine_grained_pais = (
                True if selected_grained_pai == GrainedPaiMode.FINE else False
            )

            analysis[selected_grained_pai.value] = indepth_error_rates_analysis(
                scores_test,
                labels_test,
                {"eer": eer_th},
                meta_label_info_provider(fine_grained_pais),
                bpcer_fixing_working_points,
                apcer_fixing_working_points,
            )["eer"].to_dict(label_modificator="pai")

            analysis[f"hter_{selected_grained_pai.value}"] = hter_value * 100.0

        return analysis
