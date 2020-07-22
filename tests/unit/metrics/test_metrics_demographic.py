import pytest
from gradgpad.evaluation.metrics.metrics_demographics import MetricsDemographics
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.reproducible_research.scores.scores_provider import ScoresProvider


@pytest.mark.unit
@pytest.mark.parametrize(
    "subset_scores",
    [
        ScoresProvider.get_subsets(
            approach=Approach.QUALITY_LINEAR, protocol=Protocol.GRANDTEST
        )
    ],
)
def test_should_calculate_bpcer_for_age(subset_scores):

    metrics = MetricsDemographics.from_subset_scores(subset_scores)
    bpcers = metrics.get_bpcer_age()

    assert pytest.approx(bpcers["YOUNG"], 0.01) == 28.57
    assert pytest.approx(bpcers["ADULT"], 0.01) == 16.66
    assert pytest.approx(bpcers["SENIOR"], 0.01) == 23.80


@pytest.mark.unit
@pytest.mark.parametrize(
    "subset_scores",
    [
        ScoresProvider.get_subsets(
            approach=Approach.QUALITY_LINEAR, protocol=Protocol.GRANDTEST
        )
    ],
)
def test_should_calculate_bpcer_for_sex(subset_scores):

    metrics = MetricsDemographics.from_subset_scores(subset_scores)

    bpcers = metrics.get_bpcer_sex()

    assert pytest.approx(bpcers["MALE"], 0.01) == 29.19
    assert pytest.approx(bpcers["FEMALE"], 0.01) == 18.24


@pytest.mark.unit
@pytest.mark.parametrize(
    "subset_scores",
    [
        ScoresProvider.get_subsets(
            approach=Approach.QUALITY_LINEAR, protocol=Protocol.GRANDTEST
        )
    ],
)
def test_should_calculate_bpcer_for_skin_tone(subset_scores):

    metrics = MetricsDemographics.from_subset_scores(subset_scores)

    bpcers = metrics.get_bpcer_skin_tone()

    assert pytest.approx(bpcers["LIGHT_PINK"], 0.01) == 14.70
    assert pytest.approx(bpcers["LIGHT_YELLOW"], 0.01) == 26.47
    assert pytest.approx(bpcers["MEDIUM_PINK_BROWN"], 0.01) == 11.76
    assert pytest.approx(bpcers["MEDIUM_YELLOW_BROWN"], 0.01) == 17.64
    assert pytest.approx(bpcers["MEDIUM_DARK_BROWN"], 0.01) == 17.64
    assert pytest.approx(bpcers["DARK_BROWN"], 0.01) == 23.52
