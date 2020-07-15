from enum import Enum
from typing import List


class Spai(Enum):
    GENUINE = 0
    PAI_TYPE_I = 1
    PAI_TYPE_II = 2
    PAI_TYPE_III = 3

    @staticmethod
    def options() -> List:
        return [Spai.GENUINE, Spai.PAI_TYPE_I, Spai.PAI_TYPE_II, Spai.PAI_TYPE_III]
