from enum import Enum
from typing import List


class Scenario(Enum):
    GENUINE = 0
    PAS_TYPE_I = 1
    PAS_TYPE_II = 2
    PAS_TYPE_III = 3

    @staticmethod
    def options() -> List:
        return [
            Scenario.GENUINE,
            Scenario.PAS_TYPE_I,
            Scenario.PAS_TYPE_II,
            Scenario.PAS_TYPE_III,
        ]


def get_norm_color(r, g, b):
    return r / 255, g / 255, b / 255


class ScenarioColor(Enum):
    GENUINE = "b"
    PAS_TYPE_I = get_norm_color(163, 254, 159)
    PAS_TYPE_II = get_norm_color(210, 171, 130)
    PAS_TYPE_III = get_norm_color(225, 156, 251)
