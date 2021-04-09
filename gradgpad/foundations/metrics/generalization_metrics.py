import pandas as pd

from statistics import mean

from gradgpad.foundations.annotations.grained_pai_mode import GrainedPaiMode
from gradgpad.reproducible_research import Dict
from gradgpad.tools.visualization.radar.create_apcer_detail import (
    create_apcer_by_subprotocol,
    WorkingPoint,
)
from gradgpad.foundations.scores.protocol import Protocol


class GeneralizationMetrics:
    def __init__(self,):
        self.generalization_protocols = Protocol.generalization_options()

        self.selected_working_points = {"APCER @ BPCER 10 %": WorkingPoint.BPCER_10}

        self.grained_pai_mode = GrainedPaiMode.FINE

    def _prepare_data(self, all_results):
        approach_results_protocols = {}
        for protocol in self.generalization_protocols:
            approach_results_protocols[protocol] = {}

            for approach, results in all_results.items():
                approach_results = {
                    key: value
                    for key, value in results.items()
                    if protocol.value in key
                }
                approach_results_protocols[protocol][approach] = approach_results

        apcer_details_by_working_point = {}
        for protocol, approaches_results in approach_results_protocols.items():

            for title, working_point in self.selected_working_points.items():
                apcer_detail = create_apcer_by_subprotocol(
                    approaches_results,
                    working_point,
                    f"{protocol.value}_",
                    self.grained_pai_mode,
                )

                if working_point.value not in apcer_details_by_working_point:
                    apcer_details_by_working_point[working_point.value] = {
                        protocol.value: apcer_detail
                    }
                else:
                    apcer_details_by_working_point[working_point.value][
                        protocol.value
                    ] = apcer_detail
        return apcer_details_by_working_point

    def calculate(self, all_results: Dict):

        apcer_details_by_working_point = self._prepare_data(all_results)
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
                        "wcger": max(apcers),
                    }
                    if approach not in generalization_metrics_by_approach:
                        generalization_metrics_by_approach[approach] = [apcers_data]
                    else:
                        generalization_metrics_by_approach[approach].append(apcers_data)

            data = {
                "Approach": [],
                "Protocol": [],
                "HTGER (APCER@BPCER=10%)": [],
                "WCGER (APCER@BPCER=10%)": [],
            }

            for approach, apcers_data in generalization_metrics_by_approach.items():
                for apcer_data in apcers_data:

                    data["Approach"].append(approach)
                    data["Protocol"].append(
                        apcer_data.get("protocol").replace("_", " ").upper()
                    )
                    data["HTGER (APCER@BPCER=10%)"].append(apcer_data.get("htger"))
                    data["WCGER (APCER@BPCER=10%)"].append(apcer_data.get("wcger"))

            df_by_protocol = pd.DataFrame(data, columns=list(data.keys()))

            df_mean_and_std_htger = df_by_protocol.groupby("Approach").agg(
                {"HTGER (APCER@BPCER=10%)": ["mean", "std"]}
            )
            df_mean_and_std_wcger = df_by_protocol.groupby("Approach").agg(
                {"WCGER (APCER@BPCER=10%)": ["mean", "std"]}
            )

            return df_by_protocol, df_mean_and_std_htger, df_mean_and_std_wcger

    def show(self, all_results: Dict):
        df_by_protocol, df_mean_and_std_htger, df_mean_and_std_wcger = self.calculate(
            all_results
        )
        line = 80 * "-"
        line_short = 44 * "-"

        print(
            f"The following table shows the results for Half Total Generalization Error Rate (HTGER) and the Worst Case Generalization Error Rate (WCGER) by Protocol:\n{line}"
        )
        print(df_by_protocol)
        print(f"{line}\nMean and standard deviation for HTGER:\n{line_short}")
        print(df_mean_and_std_htger)
        print(f"{line_short}\nMean and standard deviation for WCGER:\n{line_short}")
        print(df_mean_and_std_wcger)
        print(line_short)

    def save(self, all_results: Dict, output_filename: str):
        df_by_protocol, df_mean_and_std_htger, df_mean_and_std_wcger = self.calculate(
            all_results
        )
        with open(output_filename, "w") as f:
            f.write(df_by_protocol.to_markdown())
            f.write("\n")
            f.write(df_mean_and_std_htger.to_markdown())
            f.write("\n")
            f.write(df_mean_and_std_wcger.to_markdown())
