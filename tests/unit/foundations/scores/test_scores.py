import pytest

from gradgpad import (
    Age,
    Approach,
    Dataset,
    Filter,
    Protocol,
    ScoresProvider,
    Sex,
    SkinTone,
    Subset,
)

scores_approaches_test = [
    ScoresProvider.get(
        approach=approach, protocol=Protocol.GRANDTEST, subset=Subset.TEST
    )
    for approach in Approach.options_excluding(
        [Approach.AUXILIARY, Approach.CONTINUAL_LEARNING_AUXILIARY]
    )
]


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores(scores):
    assert scores.length() == 12490


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_filter_sex(scores):

    assert len(scores.filtered_by(Filter(sex=Sex.MALE))) == 1710  # 5591
    assert len(scores.filtered_by(Filter(sex=Sex.FEMALE))) == 669  # 1938


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_filter_age(scores):

    assert len(scores.filtered_by(Filter(age=Age.YOUNG))) == 2214
    assert len(scores.filtered_by(Filter(age=Age.ADULT))) == 5291  # 5153
    assert len(scores.filtered_by(Filter(age=Age.SENIOR))) == 63


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_filter_skin_tone(scores):

    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.LIGHT_PINK))) == 256
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.MEDIUM_PINK_BROWN))) == 2121
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.LIGHT_YELLOW))) == 786
    assert (
        len(scores.filtered_by(Filter(skin_tone=SkinTone.MEDIUM_YELLOW_BROWN))) == 3782
    )
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.MEDIUM_DARK_BROWN))) == 402
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.DARK_BROWN))) == 222


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_quality_rbf_scores_filter_dataset(scores):
    assert len(scores.filtered_by(Filter(dataset=Dataset.CASIA_FASD))) == 360
    assert len(scores.filtered_by(Filter(dataset=Dataset.THREEDMAD))) == 73
    assert len(scores.filtered_by(Filter(dataset=Dataset.UVAD))) == 4856
    assert len(scores.filtered_by(Filter(dataset=Dataset.SIW_M))) == 456
    assert len(scores.filtered_by(Filter(dataset=Dataset.SIW))) == 2042
    assert len(scores.filtered_by(Filter(dataset=Dataset.ROSE_YOUTU))) == 1740
    assert len(scores.filtered_by(Filter(dataset=Dataset.REPLAY_MOBILE))) == 301
    assert len(scores.filtered_by(Filter(dataset=Dataset.REPLAY_ATTACK))) == 475
    assert len(scores.filtered_by(Filter(dataset=Dataset.OULU_NPU))) == 1798
    assert len(scores.filtered_by(Filter(dataset=Dataset.MSU_MFSD))) == 118
    assert len(scores.filtered_by(Filter(dataset=Dataset.HKBU_V2))) == 168
    assert len(scores.filtered_by(Filter(dataset=Dataset.HKBU))) == 30
    assert len(scores.filtered_by(Filter(dataset=Dataset.CSMAD))) == 73


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_filter_dataset_and_sex(scores):

    assert (
        len(scores.filtered_by(Filter(sex=Sex.MALE, dataset=Dataset.CASIA_FASD))) == 300
    )
    assert (
        len(scores.filtered_by(Filter(sex=Sex.FEMALE, dataset=Dataset.CASIA_FASD)))
        == 60
    )


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_with_fair_sex_subset(scores):

    fair_sex_subset = scores.get_fair_sex_subset()

    for gender in Sex.options():
        assert len(fair_sex_subset.get(gender.name)) == 137  # 581  # 1887


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_with_fair_age_subset(scores):

    fair_age_subset = scores.get_fair_age_subset()
    for age in Age.options():
        assert len(fair_age_subset.get(age.name)) == 42  # 63


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_with_fair_skin_tone_subset(scores):

    fair_skin_tone_subset = scores.get_fair_skin_tone_subset()
    for skin_tone in SkinTone.options():
        assert len(fair_skin_tone_subset.get(skin_tone.name)) == 34  # 113


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_filter_with_random_values(scores):
    assert len(scores.filtered_by(Filter(random_values=10))) == 10


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_filter_with_pseudo_random_values(scores):
    assert len(scores.filtered_by(Filter(pseudo_random_values=10))) == 10


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_get_genuine(scores):
    assert len(scores.get_genuine()) == 2281


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_get_attacks(scores):
    assert len(scores.get_attacks()) == 10209


@pytest.mark.unit
@pytest.mark.parametrize("scores", scores_approaches_test)
def test_should_load_scores_get_numpy_scores_and_labels_filtered_by_labels(scores):
    scores, labels = scores.get_numpy_scores_and_labels_filtered_by_labels()
    assert len(scores) == 12490
    assert len(labels) == 12490
