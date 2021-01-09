from enum import Enum


class Metric(Enum):
    BPCER = 1
    APCER_AGGREGATE = 2
    APCER_SPECIFIC = 3
    BPCER_AT_APCER_10_SPECIFIC = 4
    BPCER_AT_APCER_15_SPECIFIC = 5
    BPCER_AT_APCER_40_SPECIFIC = 6
    EER = 7
    FRR = 8
    FAR = 9

    @staticmethod
    def available():
        return [
            "BPCER",
            "APCER_AGGREGATE",
            "APCER_SPECIFIC",
            "BPCER_AT_APCER_10_SPECIFIC",
            "BPCER_AT_APCER_15_SPECIFIC",
            "BPCER_AT_APCER_40_SPECIFIC",
        ]
