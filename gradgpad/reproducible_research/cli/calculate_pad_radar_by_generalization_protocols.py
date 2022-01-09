import os

from gradgpad.foundations.annotations.grained_pai_mode import GrainedPaiMode
from gradgpad.foundations.results.results_provider import ResultsProvider
from gradgpad.foundations.scores.approach import Approach
from gradgpad.foundations.scores.protocol import Protocol
from gradgpad.reproducible_research.cli.calculate_generalization_metrics import (
    calculate_generalization_metrics,
)
from gradgpad.tools.visualization.radar.create_apcer_detail import WorkingPoint
from gradgpad.tools.visualization.radar.pad_radar_protocol_plotter import (
    PadRadarProtocolPlotter,
)


def calculate_pad_radar_by_generalization_protocols(output_path: str):
    print(
        "> Novel Visualizations | Calculating PAD-radar (APCER by Generalization Protocols)..."
    )

    output_path_generalization = f"{output_path}/radar/generalization"

    approach_results_all = {
        "Quality": ResultsProvider.all(Approach.QUALITY_RBF),
        "Auxiliary": ResultsProvider.all(Approach.AUXILIARY),
    }

    approach_results_protocols = {}
    generalization_protocols = Protocol.generalization_options()

    for protocol in generalization_protocols:
        approach_results_protocols[protocol] = {}

        for approach, results in approach_results_all.items():
            approach_results = {
                key: value for key, value in results.items() if protocol.value in key
            }
            approach_results_protocols[protocol][approach] = approach_results

    apcer_details_by_working_point = {}
    for protocol, approaches_results in approach_results_protocols.items():
        selected_working_points = {
            "APCER @ BPCER 1 %": WorkingPoint.BPCER_1,
            "APCER @ BPCER 10 %": WorkingPoint.BPCER_10,
            "APCER @ BPCER 15 %": WorkingPoint.BPCER_15,
            "APCER @ BPCER 20 %": WorkingPoint.BPCER_20,
            "APCER @ BPCER 30 %": WorkingPoint.BPCER_30,
        }
        for title, working_point in selected_working_points.items():

            for grained_pai_mode in GrainedPaiMode.options():
                output_path_generalization_approach = f"{output_path_generalization}/{grained_pai_mode.value}/{protocol.value}"
                os.makedirs(output_path_generalization_approach, exist_ok=True)

                output_filename = f"{output_path_generalization_approach}/{protocol.value}_{working_point.value}_radar_chart.pdf"

                plotter = PadRadarProtocolPlotter(
                    title=title,
                    working_point=working_point,
                    grained_pai_mode=grained_pai_mode,
                    protocol=protocol,
                    format="pdf",
                )
                plotter.save(output_filename, approaches_results)

                if working_point.value not in apcer_details_by_working_point:
                    apcer_details_by_working_point[working_point.value] = {
                        protocol.value: plotter.apcer_detail
                    }
                else:
                    apcer_details_by_working_point[working_point.value][
                        protocol.value
                    ] = plotter.apcer_detail

    calculate_generalization_metrics(
        approach_results_protocols, output_path_generalization
    )

    # legacy_calculate_generalization_metrics(
    #    apcer_details_by_working_point, output_path_generalization
    # )
