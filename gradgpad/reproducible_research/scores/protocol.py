from enum import Enum
from typing import List


class Protocol(Enum):
    GRANDTEST = "grandtest"
    CROSS_DATASET = "cross_dataset"
    CROSS_DEVICE = "cross_device"
    LODO = "lodo"
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
