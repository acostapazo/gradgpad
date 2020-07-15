from enum import Enum
from typing import List


class Approach(Enum):
    QUALITY_RBF = "quality_rbf"
    QUALITY_LINEAR = "quality_linear"
    AUXILIARY = "auxiliary"

    @staticmethod
    def options() -> List:
        return [Approach.QUALITY_RBF, Approach.QUALITY_LINEAR, Approach.AUXILIARY]
