from enum import Enum
from typing import List


class CoarseGrainPai(Enum):
    PRINT = "print"
    REPLAY = "replay"
    MASK = "mask"
    MAKEUP = "makeup"
    PARTIAL = "partial"

    @staticmethod
    def options() -> List:
        return [
            CoarseGrainPai.PRINT,
            CoarseGrainPai.REPLAY,
            CoarseGrainPai.MASK,
            CoarseGrainPai.MAKEUP,
            CoarseGrainPai.PARTIAL,
        ]
