from enum import Enum
from typing import List


class Gender(Enum):
    MALE = 0
    FEMALE = 1

    @staticmethod
    def options() -> List:
        return [Gender.MALE, Gender.FEMALE]


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