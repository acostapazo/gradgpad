from enum import Enum
from typing import List


class Sex(Enum):
    MALE = 0
    FEMALE = 1

    @staticmethod
    def options() -> List:
        return [Sex.MALE, Sex.FEMALE]


class Age(Enum):
    YOUNG = 0
    ADULT = 1
    SENIOR = 2

    @staticmethod
    def options() -> List:
        return [Age.YOUNG, Age.ADULT, Age.SENIOR]


class SkinTone(Enum):
    LIGHT_PINK = 1
    LIGHT_YELLOW = 2
    MEDIUM_PINK_BROWN = 3
    MEDIUM_YELLOW_BROWN = 4
    MEDIUM_DARK_BROWN = 5
    DARK_BROWN = 6

    @staticmethod
    def options() -> List:
        return [
            SkinTone.LIGHT_PINK,
            SkinTone.LIGHT_YELLOW,
            SkinTone.MEDIUM_PINK_BROWN,
            SkinTone.MEDIUM_YELLOW_BROWN,
            SkinTone.MEDIUM_DARK_BROWN,
            SkinTone.DARK_BROWN,
        ]


SKIN_TONE_GROUP_POLICY = {
    "Yellow": ["LIGHT_YELLOW", "MEDIUM_YELLOW_BROWN"],
    "Pink": ["LIGHT_PINK", "MEDIUM_PINK_BROWN"],
    "Dark Brown": ["MEDIUM_DARK_BROWN", "DARK_BROWN"],
}
