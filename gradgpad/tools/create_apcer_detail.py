from enum import Enum
from typing import List, Dict

from dataclasses import dataclass


class WorkingPoint(Enum):
    BPCER_1 = "apcer_fixing_bpcer1"
    BPCER_5 = "apcer_fixing_bpcer5"
    BPCER_10 = "apcer_fixing_bpcer10"
    BPCER_15 = "apcer_fixing_bpcer15"
    BPCER_20 = "apcer_fixing_bpcer20"
    BPCER_25 = "apcer_fixing_bpcer25"
    BPCER_30 = "apcer_fixing_bpcer30"
    BPCER_35 = "apcer_fixing_bpcer35"
    BPCER_40 = "apcer_fixing_bpcer40"
    BPCER_45 = "apcer_fixing_bpcer45"
    BPCER_50 = "apcer_fixing_bpcer50"


def value_bpcer(working_point: WorkingPoint) -> str:
    correspondences = {
        WorkingPoint.BPCER_1: "bpcer_1",
        WorkingPoint.BPCER_5: "bpcer_5",
        WorkingPoint.BPCER_10: "bpcer_10",
        WorkingPoint.BPCER_15: "bpcer_15",
        WorkingPoint.BPCER_20: "bpcer_20",
        WorkingPoint.BPCER_25: "bpcer_25",
        WorkingPoint.BPCER_30: "bpcer_30",
        WorkingPoint.BPCER_35: "bpcer_35",
        WorkingPoint.BPCER_40: "bpcer_40",
        WorkingPoint.BPCER_45: "bpcer_45",
        WorkingPoint.BPCER_50: "bpcer_50",
    }
    return correspondences.get(working_point)


@dataclass
class ApcerDetail:
    detail_values: List
    apcers: Dict[str, List]

    def print(self):
        for approach, apcers in self.apcers.items():
            print(approach)
            for i, apcer in enumerate(apcers):
                print(f" | {self.detail_values[i]}: {apcer}")


def create_apcer_by_pai(
    results_protocol, working_point: WorkingPoint, filter_pais: List[str] = None
):
    detail_values = []
    apcers = {}
    for approach_name, result_protocol in results_protocol.items():
        apcer_per_pai_fixing_bpcer = result_protocol["specific"][
            "apcer_per_pai_fixing_bpcer"
        ]

        detail_values.clear()
        apcers[approach_name] = []

        for pai, apcers_values in sorted(apcer_per_pai_fixing_bpcer.items()):
            if filter_pais and pai not in filter_pais:
                continue
            fancy_pai = pai.replace("_", " ").upper()
            detail_values.append(fancy_pai)
            apcer = apcers_values[working_point.value]
            apcers[approach_name].append(apcer)
    return ApcerDetail(detail_values, apcers)


def create_apcer_by_subprotocol(
    results, working_point: WorkingPoint, filter_common: str = None
):
    detail_values = []
    apcers = {}

    for approach_name, result_protocols in results.items():
        detail_values.clear()
        apcers[approach_name] = []

        for subprotocol_name, result_subprotocol in sorted(result_protocols.items()):
            if filter_common:
                subprotocol_name = subprotocol_name.replace(filter_common, "")
            detail_values.append(subprotocol_name)
            apcer_subprotocol = result_subprotocol["specific"][
                "relative_working_points"
            ]["apcer"][value_bpcer(working_point)]

            apcers[approach_name].append(apcer_subprotocol)

            # print(f"{subprotocol_name} -> {apcer_subprotocol}")

    return ApcerDetail(detail_values, apcers)
