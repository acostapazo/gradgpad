import os

from gradgpad.annotations.person_attributes import SKIN_TONE_GROUP_POLICY
from gradgpad.charts import (
    create_demographic_dataframe_comparision,
    Metric,
    Demographic,
    create_metric_bar_chart_comparision,
)
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.reproducible_research.scores.scores_provider import ScoresProvider
from gradgpad.tools import group_dataframe


def calculate_demographic_bpcer_bar_chart(output_path: str):
    print("Calculating Demographic BPCER Bar Charts...")

    output_path_demographic_bar_charts = f"{output_path}/demographic/bar_charts"
    os.makedirs(output_path_demographic_bar_charts, exist_ok=True)

    metric = Metric.BPCER
    approach_scores_subset = {
        # "Quality SVM Linear": ScoresProvider.get_subsets(
        #     approach=Approach.QUALITY_LINEAR, protocol=Protocol.GRANDTEST
        # ),
        "Quality SVM RBF": ScoresProvider.get_subsets(
            approach=Approach.QUALITY_RBF, protocol=Protocol.GRANDTEST
        ),
        "Auxiliary": ScoresProvider.get_subsets(
            approach=Approach.AUXILIARY, protocol=Protocol.GRANDTEST
        ),
    }

    for demographic in Demographic.options():
        filename = f"{output_path_demographic_bar_charts}/{demographic.value}_bpcer_comparision_bar_chart.png"
        df = create_demographic_dataframe_comparision(
            metric, demographic, approach_scores_subset
        )

        create_metric_bar_chart_comparision(df, filename)

        if demographic == Demographic.SKIN_TONE:
            filename = f"{output_path_demographic_bar_charts}/{demographic.value}_grouped_bpcer_comparision_bar_chart.png"
            df = group_dataframe(df, SKIN_TONE_GROUP_POLICY)
            create_metric_bar_chart_comparision(df, filename)
