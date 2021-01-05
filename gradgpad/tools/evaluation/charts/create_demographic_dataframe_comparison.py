import pandas as pd

from typing import Dict

from gradgpad.foundations.metrics.metrics_demographics import MetricsDemographics
from gradgpad.foundations.annotations.demographic import Demographic
from gradgpad.tools import Metric


def create_dataframe_form_subset_scores(
    metric: Metric, demographic: Demographic, subset_scores
):
    data = {"Metric": [], "Error Rate (%)": [], "Protocol": []}

    metrics = MetricsDemographics.from_subset_scores(subset_scores)

    if metric != Metric.BPCER:
        raise ValueError("Only valid Metric.BPCER for now")

    metric_name = metric.name

    if demographic == Demographic.SEX:
        bpcers = metrics.get_bpcer_sex()
    elif demographic == Demographic.AGE:
        bpcers = metrics.get_bpcer_age()
    elif demographic == Demographic.SKIN_TONE:
        bpcers = metrics.get_bpcer_skin_tone()
    else:
        raise ValueError(
            f"Not available demographic value. Check available ones {Demographic.options()}"
        )

    for demographic, bpcer in bpcers.items():
        data["Metric"].append(metric_name)
        data["Error Rate (%)"].append(bpcer)
        data["Protocol"].append(demographic)
    df = pd.DataFrame(data, columns=list(data.keys()))
    return df


def create_demographic_dataframe_comparison(
    metric: Metric, demographic: Demographic, approach_subset_scores: Dict[str, Dict]
):

    # Create dataframes from result dict
    approach_dfs = {
        k: create_dataframe_form_subset_scores(metric, demographic, v)
        for k, v in approach_subset_scores.items()
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
