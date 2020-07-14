import pytest

from gradgpad.annotations.dataset import Dataset
from gradgpad.annotations.filter import Filter
from gradgpad.annotations.person_attributes import Gender, Age, SkinTone


from gradgpad.reproducible_research import quality_rbf_scores_grandtest_type_I
from gradgpad.reproducible_research import quality_linear_scores_grandtest_type_I


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores",
    [(quality_rbf_scores_grandtest_type_I), (quality_linear_scores_grandtest_type_I)],
)
def test_should_load_scores(scores):
    assert scores.length() == 12180


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores",
    [(quality_rbf_scores_grandtest_type_I), (quality_linear_scores_grandtest_type_I)],
)
def test_should_load_scores_filter_gender(scores):
    assert len(scores.filtered_by(Filter(gender=Gender.MALE))) == 5433
    assert len(scores.filtered_by(Filter(gender=Gender.FEMALE))) == 1938


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores",
    [(quality_rbf_scores_grandtest_type_I), (quality_linear_scores_grandtest_type_I)],
)
def test_should_load_scores_filter_age(scores):

    assert len(scores.filtered_by(Filter(age=Age.YOUNG))) == 2155
    assert len(scores.filtered_by(Filter(age=Age.ADULT))) == 5153
    assert len(scores.filtered_by(Filter(age=Age.SENIOR))) == 63


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores",
    [(quality_rbf_scores_grandtest_type_I), (quality_linear_scores_grandtest_type_I)],
)
def test_should_load_scores_filter_skin_tone(scores):

    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.LIGHT_PINK))) == 256
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.MEDIUM_PINK_BROWN))) == 2121
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.LIGHT_YELLOW))) == 786
    assert (
        len(scores.filtered_by(Filter(skin_tone=SkinTone.MEDIUM_YELLOW_BROWN))) == 3584
    )
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.MEDIUM_DARK_BROWN))) == 402
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.DARK_BROWN))) == 222


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores",
    [(quality_rbf_scores_grandtest_type_I), (quality_linear_scores_grandtest_type_I)],
)
def test_should_load_quality_rbf_scores_filter_dataset(scores):

    assert len(scores.filtered_by(Filter(dataset=Dataset.CASIA_FASD))) == 360
    assert len(scores.filtered_by(Filter(dataset=Dataset.THREEDMAD))) == 73
    assert len(scores.filtered_by(Filter(dataset=Dataset.UVAD))) == 4856
    assert len(scores.filtered_by(Filter(dataset=Dataset.SIW_M))) == 344
    assert len(scores.filtered_by(Filter(dataset=Dataset.SIW))) == 2042
    assert len(scores.filtered_by(Filter(dataset=Dataset.ROSE_YOUTU))) == 1542
    assert len(scores.filtered_by(Filter(dataset=Dataset.REPLAY_MOBILE))) == 301
    assert len(scores.filtered_by(Filter(dataset=Dataset.REPLAY_ATTACK))) == 475
    assert len(scores.filtered_by(Filter(dataset=Dataset.OULU_NPU))) == 1798
    assert len(scores.filtered_by(Filter(dataset=Dataset.MSU_MFSD))) == 118
    assert len(scores.filtered_by(Filter(dataset=Dataset.HKBU_V2))) == 168
    assert len(scores.filtered_by(Filter(dataset=Dataset.HKBU))) == 30
    assert len(scores.filtered_by(Filter(dataset=Dataset.CSMAD))) == 73


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores",
    [(quality_rbf_scores_grandtest_type_I), (quality_linear_scores_grandtest_type_I)],
)
def test_should_load_scores_filter_dataset_and_gender(scores):

    assert (
        len(scores.filtered_by(Filter(gender=Gender.MALE, dataset=Dataset.CASIA_FASD)))
        == 300
    )
    assert (
        len(
            scores.filtered_by(Filter(gender=Gender.FEMALE, dataset=Dataset.CASIA_FASD))
        )
        == 60
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores",
    [(quality_rbf_scores_grandtest_type_I), (quality_linear_scores_grandtest_type_I)],
)
def test_should_load_scores_with_fair_gender_subset(scores):

    fair_gender_subset = scores.get_fair_gender_subset()

    for gender in Gender.options():
        assert len(fair_gender_subset.get(gender.name)) == 1887


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores",
    [(quality_rbf_scores_grandtest_type_I), (quality_linear_scores_grandtest_type_I)],
)
def test_should_load_scores_with_fair_age_subset(scores):

    fair_age_subset = scores.get_fair_age_subset()
    for age in Age.options():
        assert len(fair_age_subset.get(age.name)) == 63


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores",
    [(quality_rbf_scores_grandtest_type_I), (quality_linear_scores_grandtest_type_I)],
)
def test_should_load_scores_with_fair_skin_tone_subset(scores):

    fair_skin_tone_subset = scores.get_fair_skin_tone_subset()
    for skin_tone in SkinTone.options():
        assert len(fair_skin_tone_subset.get(skin_tone.name)) == 113
