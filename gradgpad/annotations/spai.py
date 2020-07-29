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


def get_norm_color(r, g, b):
    return (r / 255, g / 255, b / 255)


class SpaiColor(Enum):
    GENUINE = "b"
    PAI_TYPE_I = get_norm_color(163, 254, 159)
    PAI_TYPE_II = get_norm_color(210, 171, 130)
    PAI_TYPE_III = get_norm_color(225, 156, 251)
