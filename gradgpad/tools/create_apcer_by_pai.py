from enum import Enum
from typing import List, Dict

from dataclasses import dataclass


class WorkingPoint(Enum):
    BPCER_5 = "apcer_fixing_bpcer5"
    BPCER_10 = "apcer_fixing_bpcer10"
    BPCER_15 = "apcer_fixing_bpcer15"
    BPCER_20 = "apcer_fixing_bpcer20"
    BPCER_30 = "apcer_fixing_bpcer30"
    BPCER_40 = "apcer_fixing_bpcer40"


@dataclass
class ApcerByPai:
    pais: List
    apcers: Dict[str, List]


def create_apcer_by_pai(results_protocol, working_point: WorkingPoint):
    pais = []
    apcers = {}
    for approach_name, result_protocol in results_protocol.items():

        apcer_per_pai_fixing_bpcer = result_protocol["acer_info"]["specific"][
            "apcer_per_pai_fixing_bpcer"
        ]

        pais.clear()
        apcers[approach_name] = []

        for pai, apcers_values in apcer_per_pai_fixing_bpcer.items():
            fancy_pai = pai.replace("_", " ").upper()
            pais.append(fancy_pai)
            apcer = apcers_values[working_point.value]
            apcers[approach_name].append(apcer)

    return ApcerByPai(pais, apcers)
