from enum import Enum
from typing import List


class CoarseGrainPai(Enum):
    MASK = "mask"
    MAKEUP = "makeup"
    PARTIAL = "partial"
    REPLAY = "replay"
    PRINT = "print"

    @staticmethod
    def options() -> List:
        return [
            CoarseGrainPai.MASK,
            CoarseGrainPai.MAKEUP,
            CoarseGrainPai.PARTIAL,
            CoarseGrainPai.REPLAY,
            CoarseGrainPai.PRINT,
        ]
