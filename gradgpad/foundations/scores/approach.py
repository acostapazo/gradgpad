from enum import Enum
from typing import List


class Approach(Enum):
    QUALITY_RBF = "quality_rbf"
    QUALITY_RBF_BALANCED = "quality_rbf_balanced"
    QUALITY_LINEAR = "quality_linear"
    AUXILIARY = "auxiliary"
    CONTINUAL_LEARNING_AUXILIARY = "continual_learning_auxiliary"

    @staticmethod
    def options() -> List:
        return [
            Approach.QUALITY_RBF,
            Approach.QUALITY_RBF_BALANCED,
            Approach.QUALITY_LINEAR,
            Approach.AUXILIARY,
            Approach.CONTINUAL_LEARNING_AUXILIARY,
        ]

    @staticmethod
    def options_excluding(exclude_approaches: List) -> List:
        approaches = Approach.options()
        return [
            approach for approach in approaches if approach not in exclude_approaches
        ]
