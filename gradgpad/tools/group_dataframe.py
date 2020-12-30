import statistics
from typing import Dict

import pandas as pd


def group_dataframe(df: pd.DataFrame, policy: Dict):

    metric = df.columns[1]
    try:
        metric_column_value = str(df["Metric"][0].unique()[0])
    except AttributeError:
        metric_column_value = str(df["Metric"][0])

    data_grouped = {"Metric": [], metric: [], "": [], "Approach": []}
    for key in df.keys():
        data_grouped[key] = []

    for key, values in policy.items():

        approaches = df["Approach"].unique()
        for approach in approaches:
            mean_metric = None
            for value in values:
                row = df.loc[(df[""] == value) & (df["Approach"] == approach)]
                metric_value = float(row[metric])
                if not mean_metric:
                    mean_metric = metric_value
                else:
                    mean_metric = statistics.mean([mean_metric, metric_value])

            data_grouped["Metric"].append(metric_column_value)
            data_grouped[metric].append(mean_metric)
            data_grouped[""].append(key)
            data_grouped["Approach"].append(approach)

    grouped_df = pd.DataFrame(data_grouped, columns=list(data_grouped.keys()))
    return grouped_df
