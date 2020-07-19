import os

import pandas as pd

from gradgpad.reproducible_research.results.results_provider import ResultsProvider
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol


def summary_table(output_path: str, protocol: Protocol = Protocol.GRANDTEST):
    print("Calculating Grandtest Summary Table...")

    results = {
        "Quality SVM RBF": ResultsProvider.grandtest(Approach.QUALITY_RBF),
        "Quality SVM LINEAR": ResultsProvider.grandtest(Approach.QUALITY_LINEAR),
        "Auxiliary": ResultsProvider.grandtest(Approach.AUXILIARY),
    }

    data = {
        "Protocol": [],
        "HTER": [],
        "BPCER": [],
        "ACER 5 PAI": [],
        "Worst PAI@ACER 5 PAI": [],
        "ACER 15 PAI": [],
        "Worst PAI@ACER 15 PAI": [],
    }

    for approach, approach_results in results.items():

        performance_info = approach_results[protocol.value]
        try:
            hter = performance_info.get("hter")

            # Aggregate
            aggregate_acer_info = performance_info["aggregate"]
            bpcer = aggregate_acer_info.get("bpcer")
            acer = aggregate_acer_info.get("acer")
            wrost_apcer_pai = aggregate_acer_info.get("max_apcer_pai")
            # wacer = aggregate_acer_info.get("wacer")

            # Specific
            specific_acer_info = performance_info["specific"]
            sacer = specific_acer_info.get("acer")
            wrost_specific_apcer_pai = specific_acer_info.get("max_apcer_pai")
            # wsacer = specific_acer_info.get("wacer")

            data["Protocol"].append(protocol.name)
            data["HTER"].append(hter)
            data["BPCER"].append(bpcer)
            data["ACER 5 PAI"].append(acer)
            data["Worst PAI@ACER 5 PAI"].append(wrost_apcer_pai)
            data["ACER 15 PAI"].append(sacer)
            data["Worst PAI@ACER 15 PAI"].append(wrost_specific_apcer_pai)
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
    print(md)

    with open(
        f"{output_path_summary_tables}/{protocol.value}_summary_table.md", "w"
    ) as f:
        f.write(md)
