import pandas as pd

from typing import Dict

from gradgpad.tools import create_dataframe, metric_retriever_providers


def create_demographic_dataframe_comparision(metric, approach_results: Dict[str, Dict]):

    metric_retriever = metric_retriever_providers(metric)

    # Create dataframes from result dict
    approach_dfs = {
        k: create_dataframe(metric_retriever, v) for k, v in approach_results.items()
    }

    # Add approach name to dataframes
    for approach_name, df in approach_dfs.items():
        num_rows = df.shape[0]
        df["Approach"] = [approach_name] * num_rows

    df_comparison = pd.concat(list(approach_dfs.values()))

    try:
        metric_name = str(df_comparison["Metric"][0].unique()[0])
    except AttributeError:
        metric_name = str(df_comparison["Metric"][0])
    df_comparison.rename(columns={"Error Rate (%)": f"{metric_name} (%)"}, inplace=True)
    df_comparison.rename(columns={"Protocol": ""}, inplace=True)

    return df_comparison
