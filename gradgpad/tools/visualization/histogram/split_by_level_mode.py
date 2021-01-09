from enum import Enum
from typing import List


class SplitByLabelMode(Enum):
    NONE = "none"
    PAS = "presentation_attack_scenario"
    SEX = "sex"
    AGE = "age"
    SKIN_TONE = "skin_tone"
    DATASET = "dataset"
    DATASET_GENUINE = "dataset_genuine"
    DATASET_PAS_TYPE_I = "dataset_pas_type_I"
    DATASET_PAS_TYPE_II = "dataset_pas_type_II"
    DATASET_PAS_TYPE_III = "dataset_pas_type_III"

    @staticmethod
    def options() -> List:
        return [
            SplitByLabelMode.NONE,
            SplitByLabelMode.PAS,
            SplitByLabelMode.SEX,
            SplitByLabelMode.AGE,
            SplitByLabelMode.SKIN_TONE,
            SplitByLabelMode.DATASET,
            SplitByLabelMode.DATASET_GENUINE,
            SplitByLabelMode.DATASET_PAS_TYPE_I,
            SplitByLabelMode.DATASET_PAS_TYPE_II,
            SplitByLabelMode.DATASET_PAS_TYPE_III,
        ]

    @staticmethod
    def options_for_curves():
        return [
            SplitByLabelMode.NONE,
            SplitByLabelMode.SEX,
            SplitByLabelMode.AGE,
            SplitByLabelMode.SKIN_TONE,
            SplitByLabelMode.PAS,
        ]
