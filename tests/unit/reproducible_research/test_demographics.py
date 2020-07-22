import pytest
from pandas import DataFrame

from gradgpad.annotations.person_attributes import SKIN_TONE_GROUP_POLICY
from gradgpad.charts import (
    create_metric_bar_chart_comparision,
    create_demographic_dataframe_comparision,
    Demographic,
)

from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.reproducible_research.scores.scores_provider import ScoresProvider

from gradgpad.tools import group_dataframe, Metric


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
    df = create_demographic_dataframe_comparision(
        metric, demographic, approach_subset_scores
    )
    assert isinstance(df, DataFrame)

    if policy:
        df = group_dataframe(df, policy)

    create_metric_bar_chart_comparision(df, filename)
