from enum import Enum
from typing import List


class GrainedPaiMode(Enum):
    FINE = "fine_grained_pai"
    COARSE = "coarse_grained_pai"

    @staticmethod
    def options() -> List:
        return [GrainedPaiMode.FINE, GrainedPaiMode.COARSE]
