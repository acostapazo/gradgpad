import pandas as pd

from typing import Dict

from gradgpad.tools import bpcer_metric_retriever, create_dataframe


def create_demographic_dataframe_comparision(metric, approach_results: Dict[str, Dict]):
    # TODO metric provider
    metric_retriever = bpcer_metric_retriever

    # Create dataframes from result dict
    approach_dfs = {
        k: create_dataframe(metric_retriever, v) for k, v in approach_results.items()
    }

    # Add approach name to dataframes
    for approach_name, df in approach_dfs.items():
        num_rows = df.shape[0]
        df["Approach"] = [approach_name] * num_rows

    df_comparison = pd.concat(list(approach_dfs.values()))
    df_comparison.rename(columns={"Error Rate (%)": f"{metric} (%)"}, inplace=True)
    df_comparison.rename(columns={"Protocol": ""}, inplace=True)

    return df_comparison
