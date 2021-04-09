from enum import Enum
from typing import List, Dict

from dataclasses import dataclass

from gradgpad.foundations.annotations.grained_pai_mode import GrainedPaiMode


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

    @staticmethod
    def options():
        return [
            WorkingPoint.BPCER_1,
            WorkingPoint.BPCER_5,
            WorkingPoint.BPCER_10,
            WorkingPoint.BPCER_15,
            WorkingPoint.BPCER_20,
            WorkingPoint.BPCER_25,
            WorkingPoint.BPCER_30,
            WorkingPoint.BPCER_35,
            WorkingPoint.BPCER_40,
            WorkingPoint.BPCER_45,
            WorkingPoint.BPCER_50,
        ]


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

    def sort_by_detail_values(self, target_order: List[str]):
        sorted_detail_values = []
        sorted_apcers = {}

        for target_value in target_order:
            try:
                index = self.detail_values.index(target_value)
                sorted_detail_values.append(target_value)
                for key in self.apcers.keys():
                    value_apcer = self.apcers[key][index]
                    if key not in sorted_apcers:
                        sorted_apcers[key] = [value_apcer]
                    else:
                        sorted_apcers[key].append(value_apcer)
            except ValueError:
                continue

        self.detail_values = sorted_detail_values
        self.apcers = sorted_apcers


def create_apcer_by_pai(
    results_protocol, working_point: WorkingPoint, filter_pais: List[str] = None
):
    detail_values = []
    apcers = {}
    for approach_name, result_protocol in results_protocol.items():
        apcer_per_pai_fixing_bpcer = result_protocol["fine_grained_pai"][
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
    results,
    working_point: WorkingPoint,
    filter_common: str = None,
    grained_pai_mode: GrainedPaiMode = GrainedPaiMode.FINE,
):
    detail_values = []
    apcers = {}

    for approach_name, result_protocols in results.items():
        detail_values.clear()
        apcers[approach_name] = []

        for subprotocol_name, result_subprotocol in sorted(result_protocols.items()):

            if filter_common:
                if filter_common not in subprotocol_name:
                    continue
                subprotocol_name = subprotocol_name.replace(filter_common, "")
            detail_values.append(subprotocol_name)

            apcer_subprotocol = result_subprotocol[grained_pai_mode.value][
                "relative_working_points"
            ]["apcer"][value_bpcer(working_point)]

            apcers[approach_name].append(apcer_subprotocol)

    return ApcerDetail(detail_values, apcers)
