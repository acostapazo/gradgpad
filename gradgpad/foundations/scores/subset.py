from enum import Enum
from typing import List


class Subset(Enum):
    DEVEL = "devel"
    TEST = "test"

    @staticmethod
    def options() -> List:
        return [Subset.DEVEL, Subset.TEST]
