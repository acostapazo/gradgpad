import os
from statistics import mean

import pandas as pd


def calculate_generalization_metrics(
    approach_results_protocols: dict, output_path_generalization: str
):
    os.makedirs(output_path_generalization, exist_ok=True)

    # recalculate HTGER with fine-grained ACER
    htger_with_acer = {}
    for protocol, approaches_results in approach_results_protocols.items():
        if protocol not in htger_with_acer:
            htger_with_acer[protocol.value] = {}
        for approach, results in approaches_results.items():
            acers = []
            for sub_protocol, values in results.items():
                acers.append(values["fine_grained_pai"]["acer"])
            htger = mean(acers)
            htger_with_acer[protocol.value][approach] = htger

    # recalculate HTGER with fine-grained APCER @ BPCER = 10%
    htger_with_apcer_bpcer10 = {}
    for protocol, approaches_results in approach_results_protocols.items():
        if protocol not in htger_with_apcer_bpcer10:
            htger_with_apcer_bpcer10[protocol.value] = {}
        for approach, results in approaches_results.items():
            apcers_bpcer10 = []
            for sub_protocol, values in results.items():
                apcers_bpcer10.append(
                    values["fine_grained_pai"]["relative_working_points"]["apcer"][
                        "bpcer_10"
                    ]
                )
            apcer_bpcer10 = mean(apcers_bpcer10)
            htger_with_apcer_bpcer10[protocol.value][approach] = apcer_bpcer10

    # recalculate WCGER with fine-grained APCER
    wcgers = {}
    for protocol, approaches_results in approach_results_protocols.items():
        if protocol not in wcgers:
            wcgers[protocol.value] = {}
        for approach, results in approaches_results.items():
            apcers = []
            for sub_protocol, values in results.items():
                apcers.append(
                    values["fine_grained_pai"]["relative_working_points"]["apcer"][
                        "bpcer_10"
                    ]
                )
            wcger = max(apcers)
            wcgers[protocol.value][approach] = wcger

    data = {
        "Approach": [],
        "Protocol": [],
        "HTGER (ACER)": [],
        "WCGER (APCER@BPCER=10%)": [],
        "Average (APCER@BPCER=10%)": [],
    }

    for approach in ["Quality", "Auxiliary"]:
        for protocol, htger_data in htger_with_acer.items():

            data["Approach"].append(approach)
            data["Protocol"].append(protocol.replace("_", " ").upper())

            htger_with_acer_value = htger_with_acer.get(protocol, {}).get(approach)
            data["HTGER (ACER)"].append(htger_with_acer_value)

            wcger_value = wcgers.get(protocol, {}).get(approach)
            data["WCGER (APCER@BPCER=10%)"].append(wcger_value)

            htger_apcer_bpcer10 = htger_with_apcer_bpcer10.get(protocol, {}).get(
                approach
            )
            data["Average (APCER@BPCER=10%)"].append(htger_apcer_bpcer10)

    df_by_protocol = pd.DataFrame(data, columns=list(data.keys()))

    df_htger = df_by_protocol.groupby("Approach").agg({"HTGER (ACER)": ["mean", "std"]})
    df_wcger = df_by_protocol.groupby("Approach").agg(
        {"WCGER (APCER@BPCER=10%)": ["mean", "std"]}
    )

    filename = f"{output_path_generalization}/generalization_metrics.md"

    with open(filename, "w") as f:
        f.write(df_by_protocol.to_markdown())
        f.write("\n\n")
        f.write(df_htger.to_markdown())
        f.write("\n\n")
        f.write(df_wcger.to_markdown())


def legacy_calculate_generalization_metrics(
    apcer_details_by_working_point, output_path_generalization
):
    output_path_generalization_metrics = f"{output_path_generalization}/metrics"
    os.makedirs(output_path_generalization_metrics, exist_ok=True)
    for (
        working_point_value,
        protocols_apcer_detail,
    ) in apcer_details_by_working_point.items():
        generalization_metrics_by_approach = {}
        for protocol_name, apcer_detail in protocols_apcer_detail.items():
            for approach, apcers in apcer_detail.apcers.items():
                apcers_data = {
                    "protocol": protocol_name,
                    "htger": mean(apcers),
                    "ager": max(apcers),
                }
                if approach not in generalization_metrics_by_approach:
                    generalization_metrics_by_approach[approach] = [apcers_data]
                else:
                    generalization_metrics_by_approach[approach].append(apcers_data)

        data = {
            "Approach": [],
            "Protocol": [],
            "HTGER (APCER@BPCER=10%)": [],
            "AGER (APCER@BPCER=10%)": [],
        }

        for approach, apcers_data in generalization_metrics_by_approach.items():
            for apcer_data in apcers_data:
                data["Approach"].append(approach)
                data["Protocol"].append(apcer_data.get("protocol"))
                data["HTGER (APCER@BPCER=10%)"].append(apcer_data.get("htger"))
                data["AGER (APCER@BPCER=10%)"].append(apcer_data.get("ager"))

        df_by_protocol = pd.DataFrame(data, columns=list(data.keys()))

        df_htger = df_by_protocol.groupby("Approach").agg(
            {"HTGER (APCER@BPCER=10%)": ["mean", "std"]}
        )
        df_ager = df_by_protocol.groupby("Approach").agg(
            {"AGER (APCER@BPCER=10%)": ["mean", "std"]}
        )

        filename = (
            f"{output_path_generalization_metrics}/metrics_{working_point_value}.md"
        )

        with open(filename, "w") as f:
            f.write(df_by_protocol.to_markdown())
            f.write("\n")
            f.write(df_htger.to_markdown())
            f.write("\n")
            f.write(df_ager.to_markdown())
