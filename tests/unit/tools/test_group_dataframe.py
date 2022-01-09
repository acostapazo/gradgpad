import pytest
from pandas import DataFrame

from gradgpad import (
    SKIN_TONE_GROUP_POLICY,
    Approach,
    Demographic,
    Protocol,
    ScoresProvider,
)
from gradgpad.tools import Metric, group_dataframe
from gradgpad.tools.visualization.charts.create_demographic_dataframe_comparison import (
    create_demographic_dataframe_comparison,
)


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

    df = create_demographic_dataframe_comparison(
        metric, demographic, approach_scores_subset
    )

    df = group_dataframe(df, SKIN_TONE_GROUP_POLICY)

    assert isinstance(df, DataFrame)
