from enum import Enum
from typing import List


class SplitByLabelMode(Enum):
    NONE = "none"
    PAS = "presentation_attack_scenario"
    SEX = "sex"
    AGE = "age"
    SKIN_TONE = "skin_tone"

    @staticmethod
    def options() -> List:
        return [
            SplitByLabelMode.NONE,
            SplitByLabelMode.PAS,
            SplitByLabelMode.SEX,
            SplitByLabelMode.AGE,
            SplitByLabelMode.SKIN_TONE,
        ]
