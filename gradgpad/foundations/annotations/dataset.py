from enum import Enum
from typing import List


class Dataset(Enum):
    CASIA_FASD = "casia-fasd"
    THREEDMAD = "threedmad"
    UVAD = "uvad"
    SIW_M = "siw-m"
    SIW = "siw"
    ROSE_YOUTU = "rose-youtu"
    REPLAY_MOBILE = "replay-mobile"
    REPLAY_ATTACK = "replay-attack"
    OULU_NPU = "oulu-npu"
    MSU_MFSD = "msu-mfsd"
    HKBU_V2 = "hkbuv2"
    HKBU = "hkbu"
    CSMAD = "csmad"

    @staticmethod
    def options() -> List:
        return [
            Dataset.CASIA_FASD,
            Dataset.THREEDMAD,
            Dataset.UVAD,
            Dataset.SIW_M,
            Dataset.SIW,
            Dataset.ROSE_YOUTU,
            Dataset.REPLAY_MOBILE,
            Dataset.REPLAY_ATTACK,
            Dataset.OULU_NPU,
            Dataset.MSU_MFSD,
            Dataset.HKBU_V2,
            Dataset.HKBU,
            Dataset.CSMAD,
        ]
