from enum import Enum
from typing import List


class GrainedPaiMode(Enum):
    FINE = "fine-grained-pais"
    COARSE = "coarse-grained-pais"

    @staticmethod
    def options() -> List:
        return [GrainedPaiMode.FINE, GrainedPaiMode.COARSE]
