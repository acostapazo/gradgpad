import pytest
from pandas import DataFrame

from gradgpad import (
    Approach,
    Protocol,
    ScoresProvider,
    Demographic,
    SKIN_TONE_GROUP_POLICY,
    Metric,
)
from gradgpad.tools import group_dataframe
from gradgpad.tools.evaluation.charts import create_metric_bar_chart_comparison
from gradgpad.tools.evaluation.charts.create_demographic_dataframe_comparison import (
    create_demographic_dataframe_comparison,
)

APPROACH_SCORES_SUBSET = {
    "Quality SVM Linear": ScoresProvider.get_subsets(
        approach=Approach.QUALITY_LINEAR, protocol=Protocol.GRANDTEST
    ),
    "Quality SVM RBF": ScoresProvider.get_subsets(
        approach=Approach.QUALITY_RBF, protocol=Protocol.GRANDTEST
    ),
    "Auxiliary": ScoresProvider.get_subsets(
        approach=Approach.AUXILIARY, protocol=Protocol.GRANDTEST
    ),
}


@pytest.mark.unit
@pytest.mark.parametrize(
    "metric, demographic, approach_subset_scores, policy, filename",
    [
        (
            Metric.BPCER,
            Demographic.SEX,
            APPROACH_SCORES_SUBSET,
            None,
            "tests/output/sex_bpcer_comparision_bar_chart.png",
        ),
        (
            Metric.BPCER,
            Demographic.AGE,
            APPROACH_SCORES_SUBSET,
            None,
            "tests/output/age_bpcer_comparision_bar_chart.png",
        ),
        (
            Metric.BPCER,
            Demographic.SKIN_TONE,
            APPROACH_SCORES_SUBSET,
            None,
            "tests/output/skin_tone_bpcer_comparision_bar_chart.png",
        ),
        (
            Metric.BPCER,
            Demographic.SKIN_TONE,
            {
                "Quality SVM Linear": ScoresProvider.get_subsets(
                    approach=Approach.QUALITY_LINEAR, protocol=Protocol.GRANDTEST
                ),
                "Quality SVM RBF": ScoresProvider.get_subsets(
                    approach=Approach.QUALITY_RBF, protocol=Protocol.GRANDTEST
                ),
                "Auxiliary": ScoresProvider.get_subsets(
                    approach=Approach.AUXILIARY, protocol=Protocol.GRANDTEST
                ),
            },
            SKIN_TONE_GROUP_POLICY,
            "tests/output/skin_tone_bpcer_grouped_comparision_bar_chart.png",
        ),
    ],
)
def test_should_success_create_demographic_df_and_comparision_bar_chart(
    metric, demographic, approach_subset_scores, policy, filename
):
    df = create_demographic_dataframe_comparison(
        metric, demographic, approach_subset_scores
    )
    assert isinstance(df, DataFrame)

    if policy:
        df = group_dataframe(df, policy)

    create_metric_bar_chart_comparison(df, filename)
