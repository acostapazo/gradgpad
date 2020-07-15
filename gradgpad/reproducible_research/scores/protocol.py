from enum import Enum
from typing import List


class Protocol(Enum):
    GRANDTEST = "grandtest_train_type_pai_i_test_all"
    CROSS_DATASET = "cross_dataset_test"
    CROSS_DEVICE = "cross_device_test"
    LODO = "leave_other_datasets_out"
    UNSEEN_ATTACK = "unseen_attack"

    @staticmethod
    def options() -> List:
        return [
            Protocol.GRANDTEST,
            Protocol.CROSS_DATASET,
            Protocol.CROSS_DEVICE,
            Protocol.LODO,
            Protocol.UNSEEN_ATTACK,
        ]


class SubProtocol(Enum):
    HKBU = "hkbu"
    HKBUV2 = "hkbu"
    LODO = "leave_other_datasets_out"
    UNSEEN_ATTACK = "unseen_attack"

    @staticmethod
    def options() -> List:
        return [
            Protocol.GRANDTEST,
            Protocol.CROSS_DATASET,
            Protocol.LODO,
            Protocol.UNSEEN_ATTACK,
        ]
