from enum import Enum
from typing import List


class CoarseGrainedPai(Enum):
    MASK = "mask"
    MAKEUP = "makeup"
    PARTIAL = "partial"
    REPLAY = "replay"
    PRINT = "print"

    @staticmethod
    def options() -> List:
        return [
            CoarseGrainedPai.MASK,
            CoarseGrainedPai.MAKEUP,
            CoarseGrainedPai.PARTIAL,
            CoarseGrainedPai.REPLAY,
            CoarseGrainedPai.PRINT,
        ]
