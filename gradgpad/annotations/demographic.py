from enum import Enum
from typing import List


class Demographic(Enum):
    SEX = "sex"
    AGE = "age"
    SKIN_TONE = "skin_tone"

    @staticmethod
    def options() -> List:
        return [Demographic.SEX, Demographic.AGE, Demographic.SKIN_TONE]
