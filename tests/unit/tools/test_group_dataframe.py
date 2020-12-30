import pytest
from pandas import DataFrame

from gradgpad.foundations.annotations.person_attributes import SKIN_TONE_GROUP_POLICY
from gradgpad.evaluation.charts import (
    create_demographic_dataframe_comparision,
    Demographic,
)
from gradgpad.foundations.scores.approach import Approach
from gradgpad.foundations.scores.protocol import Protocol
from gradgpad.foundations.scores.scores_provider import ScoresProvider

from gradgpad.tools import group_dataframe, Metric


@pytest.mark.unit
def test_should_group_dataframe():
    metric = Metric.BPCER
    demographic = Demographic.SKIN_TONE
    approach_scores_subset = {
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

    df = create_demographic_dataframe_comparision(
        metric, demographic, approach_scores_subset
    )

    df = group_dataframe(df, SKIN_TONE_GROUP_POLICY)

    assert isinstance(df, DataFrame)
