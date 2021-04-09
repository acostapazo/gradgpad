import pytest
from gradgpad.foundations.metrics.metrics import Metrics
from gradgpad.foundations.scores.approach import Approach
from gradgpad.foundations.scores.protocol import Protocol
from gradgpad.foundations.scores.scores_provider import ScoresProvider
from gradgpad.foundations.scores.subset import Subset


@pytest.mark.unit
@pytest.mark.parametrize(
    "devel_scores,test_scores",
    [
        (
            ScoresProvider.get(
                approach=Approach.QUALITY_LINEAR,
                protocol=Protocol.GRANDTEST,
                subset=Subset.DEVEL,
            ),
            ScoresProvider.get(
                approach=Approach.QUALITY_LINEAR,
                protocol=Protocol.GRANDTEST,
                subset=Subset.TEST,
            ),
        )
    ],
)
def test_should_calculate_eer_for_devel_and_test(devel_scores, test_scores):

    metrics = Metrics(devel_scores, test_scores)
    assert pytest.approx(metrics.get_eer(Subset.DEVEL), 0.01) == 0.269
    assert pytest.approx(metrics.get_eer(Subset.TEST), 0.01) == 0.246


@pytest.mark.unit
@pytest.mark.parametrize(
    "devel_scores,test_scores",
    [
        (
            ScoresProvider.get(
                approach=Approach.QUALITY_RBF,
                protocol=Protocol.GRANDTEST,
                subset=Subset.DEVEL,
            ),
            ScoresProvider.get(
                approach=Approach.QUALITY_RBF,
                protocol=Protocol.GRANDTEST,
                subset=Subset.TEST,
            ),
        )
    ],
)
def test_should_calculate_indeepth_analysis(devel_scores, test_scores):

    metrics = Metrics(devel_scores, test_scores)
    bpcer_fixing_working_points = [0.10]
    apcer_fixing_working_points = [0.10]

    indepth_analysis = metrics.get_indepth_analysis(
        bpcer_fixing_working_points, apcer_fixing_working_points
    )

    assert pytest.approx(indepth_analysis["fine_grained_pai"]["acer"], 0.01) == 59.60
    assert pytest.approx(indepth_analysis["coarse_grained_pai"]["acer"], 0.01) == 36.06
