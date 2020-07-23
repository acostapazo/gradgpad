import os

from gradgpad.charts.create_radar_chart_comparision import (
    create_radar_chart_comparision,
)
from gradgpad.reproducible_research.results.results_provider import ResultsProvider
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.tools.create_apcer_detail import WorkingPoint, create_apcer_by_subprotocol


def calculate_apcer_generalization_protocols(output_path: str):
    print("Calculating APCER for Generalization Protocols...")

    output_path_generalization = f"{output_path}/radar/generalization"

    approach_results_all = {
        "Quality SVM RBF": ResultsProvider.all(Approach.QUALITY_RBF),
        "Quality SVM LINEAR": ResultsProvider.all(Approach.QUALITY_LINEAR),
        "Auxiliary": ResultsProvider.all(Approach.AUXILIARY),
    }

    approach_results_protocols = {}
    generalization_protocols = [
        protocol for protocol in Protocol.options() if protocol != Protocol.GRANDTEST
    ]
    for protocol in generalization_protocols:
        approach_results_protocols[protocol.value] = {}
        for approach, results in approach_results_all.items():
            approach_results = {
                key: value for key, value in results.items() if protocol.value in key
            }
            approach_results_protocols[protocol.value][approach] = approach_results

    for protocol_name, approach_results in approach_results_protocols.items():

        selected_working_points = {
            "APCER @ BPCER 10 %": WorkingPoint.BPCER_10,
            "APCER @ BPCER 15 %": WorkingPoint.BPCER_15,
            "APCER @ BPCER 20 %": WorkingPoint.BPCER_20,
        }
        for title, working_point in selected_working_points.items():

            output_path_generalization_approach = (
                f"{output_path_generalization}/{protocol_name}"
            )
            os.makedirs(output_path_generalization_approach, exist_ok=True)

            filename = f"{output_path_generalization_approach}/{protocol_name}_{working_point.value}_radar_chart.png"

            apcer_detail = create_apcer_by_subprotocol(
                approach_results, working_point, f"{protocol_name}_"
            )
            create_radar_chart_comparision(title, apcer_detail, filename)