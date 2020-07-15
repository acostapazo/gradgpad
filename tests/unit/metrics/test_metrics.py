import pytest
from gradgpad.metrics.metrics import Metrics
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.reproducible_research.scores.scores_provider import ScoresProvider
from gradgpad.reproducible_research.scores.subset import Subset


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

    assert pytest.approx(metrics.get_eer_devel(), 0.1) == 0.269
    assert (
        pytest.approx(metrics.get_eer_test(), 0.1) == 0.269
    )  # TODO suspicious, same file for devel and test
