import os
from gradgpad.charts.create_radar_chart_comparision import (
    create_radar_chart_comparision,
)
from gradgpad.reproducible_research.cli.calculate_generalization_metrics import (
    calculate_generalization_metrics,
)
from gradgpad.reproducible_research.results.results_provider import ResultsProvider
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.tools.create_apcer_detail import WorkingPoint, create_apcer_by_subprotocol


DATASET_CORRESPONDENCES = {
    "casia-fasd": "CASIA-FASD",
    "uvad": "UVAD",
    "threedmad": "3DMAD",
    "siw-m": "SiW-M",
    "siw": "SiW",
    "rose-youtu": "Rose-Youtu",
    "replay-mobile": "Replay-Mobile",
    "replay-attack": "Replay-Attack",
    "oulu-npu": "Oulu-NPU",
    "msu-mfsd": "MSU-MFSD",
    "hkbuV2": "$HKBU_{v2}$",
    "hkbu": "$HKBU_{v1}$",
    "csmad": "CSMAD",
}
CROSS_DEVICE_CORRESPONDENCES = {
    "digital_camera": "Digital Camera",
    "mobile_tablet": "Mobile | Tablet",
    "webcam": "Webcam",
}

UNSEEN_ATTACK_CORRESPONDENCES = {
    "mask": "Mask",
    "makeup": "Makeup",
    "partial": "Partial",
    "replay": "Replay",
    "print": "Print",
}
CORRESPONDENCES = {
    "lodo": DATASET_CORRESPONDENCES,
    "cross_dataset": DATASET_CORRESPONDENCES,
    "intradataset": DATASET_CORRESPONDENCES,
    "cross_device": CROSS_DEVICE_CORRESPONDENCES,
    "unseen_attack": UNSEEN_ATTACK_CORRESPONDENCES,
}


def calculate_apcer_generalization_protocols(output_path: str):
    print("Calculating APCER for Generalization Protocols...")

    output_path_generalization = f"{output_path}/radar/generalization"

    # approach_results_all = {
    #     "Quality SVM RBF": ResultsProvider.all(Approach.QUALITY_RBF),
    #     "Quality SVM LINEAR": ResultsProvider.all(Approach.QUALITY_LINEAR),
    #     "Auxiliary": ResultsProvider.all(Approach.AUXILIARY),
    # }

    approach_results_all = {
        "Quality": ResultsProvider.all(Approach.QUALITY_RBF),
        "Auxiliary": ResultsProvider.all(Approach.AUXILIARY),
    }

    approach_results_protocols = {}
    generalization_protocols = Protocol.generalization_options()

    for protocol in generalization_protocols:
        approach_results_protocols[protocol.value] = {}

        for approach, results in approach_results_all.items():
            approach_results = {
                key: value for key, value in results.items() if protocol.value in key
            }
            approach_results_protocols[protocol.value][approach] = approach_results

    apcer_details_by_working_point = {}
    for protocol_name, approach_results in approach_results_protocols.items():
        selected_working_points = {
            "APCER @ BPCER 10 %": WorkingPoint.BPCER_10,
            "APCER @ BPCER 15 %": WorkingPoint.BPCER_15,
            "APCER @ BPCER 20 %": WorkingPoint.BPCER_20,
        }
        for title, working_point in selected_working_points.items():

            for type_apcer in ["specific", "aggregate"]:
                output_path_generalization_approach = (
                    f"{output_path_generalization}/{type_apcer}/{protocol_name}"
                )
                os.makedirs(output_path_generalization_approach, exist_ok=True)

                filename = f"{output_path_generalization_approach}/{protocol_name}_{working_point.value}_radar_chart.png"

                apcer_detail = create_apcer_by_subprotocol(
                    approach_results, working_point, f"{protocol_name}_", type_apcer
                )
                if working_point.value not in apcer_details_by_working_point:
                    apcer_details_by_working_point[working_point.value] = {
                        protocol_name: apcer_detail
                    }
                else:
                    apcer_details_by_working_point[working_point.value][
                        protocol_name
                    ] = apcer_detail

                try:
                    create_radar_chart_comparision(
                        title,
                        apcer_detail,
                        filename,
                        CORRESPONDENCES.get(protocol_name),
                        20,
                    )
                except ZeroDivisionError as exec:
                    print(exec)
                    print(f"Error on create_apcer_by_subprotocol: {protocol_name}")
                    print(f"apcer_detail: {apcer_detail}")
                    print(f"CORRESPONDENCE: {CORRESPONDENCES.get(protocol_name)}")

    calculate_generalization_metrics(
        apcer_details_by_working_point, output_path_generalization
    )
