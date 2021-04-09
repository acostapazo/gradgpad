from enum import Enum
from typing import List


class Protocol(Enum):
    GRANDTEST = "grandtest"
    GRANDTEST_TYPE_I_AND_II = "grandtest_type_i_and_ii"
    GRANDTEST_SEX_50_50 = "grandtest_sex_50_50"
    GRANDTEST_SEX_80_20 = "grandtest_sex_80_20"
    GRANDTEST_SEX_90_10 = "grandtest_sex_90_10"
    CROSS_DATASET = "cross_dataset"
    CROSS_DEVICE = "cross_device"
    LODO = "lodo"
    UNSEEN_ATTACK = "unseen_attack"
    INTRADATASET = "intradataset"

    @staticmethod
    def options() -> List:
        return [
            Protocol.GRANDTEST,
            Protocol.GRANDTEST_SEX_50_50,
            Protocol.GRANDTEST_SEX_80_20,
            Protocol.GRANDTEST_SEX_90_10,
            Protocol.CROSS_DATASET,
            Protocol.CROSS_DEVICE,
            Protocol.LODO,
            Protocol.UNSEEN_ATTACK,
            Protocol.INTRADATASET,
        ]

    @staticmethod
    def generalization_options() -> List:
        return [
            Protocol.CROSS_DATASET,
            Protocol.CROSS_DEVICE,
            Protocol.LODO,
            Protocol.UNSEEN_ATTACK,
        ]

    @staticmethod
    def grandtest_options() -> List:
        return [
            Protocol.GRANDTEST,
            Protocol.GRANDTEST_SEX_50_50,
            Protocol.GRANDTEST_SEX_80_20,
            Protocol.GRANDTEST_SEX_90_10,
        ]
