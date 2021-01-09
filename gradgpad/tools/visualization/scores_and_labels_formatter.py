from typing import List

from gradgpad.tools.visualization.histogram.split_by_level_mode import SplitByLabelMode
from gradgpad.foundations.scores import Scores, Scenario


class ScoresAndLabelsFormatter:
    @staticmethod
    def execute(
        scores: Scores,
        split_by_label_mode: SplitByLabelMode = SplitByLabelMode.NONE,
        exclude_labels: List[int] = None,
    ):

        np_scores = scores.get_numpy_scores()
        split_labels_correspondences = {}

        if split_by_label_mode == SplitByLabelMode.NONE:
            np_labels = scores.get_numpy_labels()
        elif split_by_label_mode == SplitByLabelMode.PAS:
            np_labels = scores.get_numpy_labels_by_scenario()
            split_labels_correspondences = {
                0: "Genuine",
                1: "PAS Type I",
                2: "PAS Type II",
                3: "PAS Type III",
            }
        elif split_by_label_mode == SplitByLabelMode.SEX:
            np_labels = scores.get_numpy_labels_by_sex()
            split_labels_correspondences = {-1: "ATTACK", 0: "MALE", 1: "FEMALE"}
        elif split_by_label_mode == SplitByLabelMode.AGE:
            np_labels = scores.get_numpy_labels_by_age()
            split_labels_correspondences = {
                -1: "ATTACK",
                0: "YOUNG",
                1: "ADULT",
                2: "SENIOR",
            }
        elif split_by_label_mode == SplitByLabelMode.SKIN_TONE:
            np_labels = scores.get_numpy_labels_by_skin_tone()
            split_labels_correspondences = {
                -1: "ATTACK",
                1: "LIGHT_PINK",
                2: "LIGHT_YELLOW",
                3: "MEDIUM_PINK_BROWN",
                4: "MEDIUM_YELLOW_BROWN",
                5: "MEDIUM_DARK_BROWN",
                6: "DARK_BROWN",
            }
        elif SplitByLabelMode.DATASET.value in split_by_label_mode.value:
            if not exclude_labels:
                exclude_labels = [-1]

            split_labels_correspondences = {
                0: "CASIA-FASD",
                1: "CSMAD",
                2: "HKBU",
                3: "HKBU V2",
                4: "MSU-MFSD",
                5: "Oulu-NPU",
                6: "Replay-Attack",
                7: "Replay-Mobile",
                8: "Rose-Youtu",
                9: "SiW",
                10: "SiW-M",
                11: "3D-MAD",
                12: "UVAD",
            }

            if split_by_label_mode == SplitByLabelMode.DATASET_GENUINE:
                np_labels = scores.get_numpy_labels_by_dataset_and_scenario(
                    Scenario.GENUINE
                )
            elif split_by_label_mode == SplitByLabelMode.DATASET_PAS_TYPE_I:
                np_labels = scores.get_numpy_labels_by_dataset_and_scenario(
                    Scenario.PAS_TYPE_I
                )
            elif split_by_label_mode == SplitByLabelMode.DATASET_PAS_TYPE_II:
                np_labels = scores.get_numpy_labels_by_dataset_and_scenario(
                    Scenario.PAS_TYPE_II
                )
                split_labels_correspondences = {0: "Rose-Youtu", 1: "SiW-M"}
            elif split_by_label_mode == SplitByLabelMode.DATASET_PAS_TYPE_III:
                np_labels = scores.get_numpy_labels_by_dataset_and_scenario(
                    Scenario.PAS_TYPE_III
                )
                split_labels_correspondences = {0: "SiW-M"}
            else:
                np_labels = scores.get_numpy_labels_by_dataset()

        else:
            np_labels = scores.get_numpy_labels()
        return np_scores, np_labels, split_labels_correspondences
