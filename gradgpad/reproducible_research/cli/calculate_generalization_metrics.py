import os
import pandas as pd

from statistics import mean


def calculate_generalization_metrics(
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
