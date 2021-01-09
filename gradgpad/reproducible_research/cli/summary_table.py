import os

import pandas as pd

from gradgpad.foundations.results.results_provider import ResultsProvider
from gradgpad.foundations.scores.approach import Approach
from gradgpad.foundations.scores.protocol import Protocol


def summary_table(output_path: str, protocol: Protocol = Protocol.GRANDTEST):
    print("> Grandtest Protocol | Calculating a Summary Table...")

    results = {
        "Quality SVM RBF": ResultsProvider.grandtest(Approach.QUALITY_RBF),
        # "Quality SVM LINEAR": ResultsProvider.grandtest(Approach.QUALITY_LINEAR),
        "Auxiliary": ResultsProvider.grandtest(Approach.AUXILIARY),
    }

    data = {
        "Protocol": [],
        "HTER": [],
        "ACER (Coarse-grain)": [],
        "APCER@BPCER=10% (Coarse-grain)": [],
        "ACER (Fine-grain)": [],
        "APCER@BPCER=10% (Fine-grain)": [],
        # "Worst PAI@ACER 5 PAI": [],
        # "Worst PAI@ACER 13 PAI": [],
    }

    for approach, approach_results in results.items():

        performance_info = approach_results[protocol.value]
        try:
            hter_fine_grained_pai = performance_info.get("hter_fine_grained_pai")
            hter_coarse_grained_pai = performance_info.get("hter_coarse_grained_pai")

            assert hter_fine_grained_pai == hter_coarse_grained_pai

            # Aggregate
            aggregate_acer_info = performance_info["coarse_grained_pai"]
            # bpcer = aggregate_acer_info.get("bpcer")
            acer = aggregate_acer_info.get("acer")
            # wrost_apcer_pai = aggregate_acer_info.get("max_apcer_pai")
            # wacer = aggregate_acer_info.get("wacer")
            apcer_bpcer10 = (
                aggregate_acer_info.get("relative_working_points", {})
                .get("apcer", {})
                .get("bpcer_10")
            )

            # Specific
            specific_acer_info = performance_info["fine_grained_pai"]
            sacer = specific_acer_info.get("acer")
            # wrost_specific_apcer_pai = specific_acer_info.get("max_apcer_pai")
            # wsacer = specific_acer_info.get("wacer")
            sapcer_bpcer10 = (
                specific_acer_info.get("relative_working_points", {})
                .get("apcer", {})
                .get("bpcer_10")
            )

            data["Protocol"].append(protocol.name)
            data["HTER"].append(hter_coarse_grained_pai)
            data["ACER (Coarse-grain)"].append(acer)
            data["APCER@BPCER=10% (Coarse-grain)"].append(apcer_bpcer10)
            data["ACER (Fine-grain)"].append(sacer)
            data["APCER@BPCER=10% (Fine-grain)"].append(sapcer_bpcer10)

            # data["Worst PAI@ACER 5 PAI"].append(wrost_apcer_pai)
            # data["Worst PAI@ACER 13 PAI"].append(wrost_specific_apcer_pai)
        except Exception:
            pass

    df = pd.DataFrame(data, index=results.keys(), columns=data.keys())

    output_path_summary_tables = f"{output_path}/summary_tables"
    os.makedirs(output_path_summary_tables, exist_ok=True)

    df.to_csv(
        f"{output_path_summary_tables}/{protocol.value}_summary_table.csv",
        sep="|",
        index=False,
    )
    md = df.to_markdown()
    # print(md)

    with open(
        f"{output_path_summary_tables}/{protocol.value}_summary_table.md", "w"
    ) as f:
        f.write(md)
