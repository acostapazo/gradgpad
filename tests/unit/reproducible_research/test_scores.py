import pytest

from gradgpad.annotations.dataset import Dataset
from gradgpad.annotations.filter import Filter
from gradgpad.annotations.person_attributes import Gender, Age, SkinTone


@pytest.mark.unit
def test_should_load_quality_rbf_scores():
    from gradgpad.reproducible_research import quality_rbf_scores_grandtest_type_I

    assert quality_rbf_scores_grandtest_type_I.length() == 12180


@pytest.mark.unit
def test_should_load_quality_linear_scores():
    from gradgpad.reproducible_research import quality_linear_scores_grandtest_type_I

    assert quality_linear_scores_grandtest_type_I.length() == 12180


@pytest.mark.unit
def test_should_load_quality_rbf_scores_filter_gender():
    from gradgpad.reproducible_research import (
        quality_rbf_scores_grandtest_type_I as scores,
    )

    assert len(scores.filtered_by(Filter(gender=Gender.MALE))) == 5433
    assert len(scores.filtered_by(Filter(gender=Gender.FEMALE))) == 1938


@pytest.mark.unit
def test_should_load_quality_rbf_scores_filter_age():
    from gradgpad.reproducible_research import (
        quality_rbf_scores_grandtest_type_I as scores,
    )

    assert len(scores.filtered_by(Filter(age=Age.YOUNG))) == 2155
    assert len(scores.filtered_by(Filter(age=Age.ADULT))) == 5153
    assert len(scores.filtered_by(Filter(age=Age.SENIOR))) == 63


@pytest.mark.unit
def test_should_load_quality_rbf_scores_filter_skin_tone():
    from gradgpad.reproducible_research import (
        quality_rbf_scores_grandtest_type_I as scores,
    )

    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.LIGHT_PINK))) == 256
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.MEDIUM_PINK_BROWN))) == 2121
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.LIGHT_YELLOW))) == 786
    assert (
        len(scores.filtered_by(Filter(skin_tone=SkinTone.MEDIUM_YELLOW_BROWN))) == 3584
    )
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.MEDIUM_DARK_BROWN))) == 402
    assert len(scores.filtered_by(Filter(skin_tone=SkinTone.DARK_BROWN))) == 222


@pytest.mark.unit
def test_should_load_quality_rbf_scores_filter_dataset():
    from gradgpad.reproducible_research import (
        quality_rbf_scores_grandtest_type_I as scores,
    )

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
def test_should_load_quality_rbf_scores_filter_dataset_and_gender():
    from gradgpad.reproducible_research import (
        quality_rbf_scores_grandtest_type_I as scores,
    )

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


# @pytest.mark.unit
# def test_should_load_quality_rbf_scores_filter_protocols():
#     from gradgpad.reproducible_research import (
#         quality_rbf_scores_grandtest_type_I as scores,
#     )
#
#     def get_smallest_length(x):
#         return [
#             k for k in x.keys() if len(x.get(k)) == min([len(n) for n in x.values()])
#         ]
#
#     min_value = {}
#     for dataset in Dataset.options():
#         filters = {
#             "male": Filter(gender=Gender.MALE, dataset=dataset),
#             "female": Filter(gender=Gender.FEMALE, dataset=dataset),
#         }
#
#         filtered_scores = {}
#         for key, filter in filters.items():
#             filtered_scores[key] = scores.filtered_by(filter)
#
#         smallest_key = get_smallest_length(filtered_scores)[0]
#         min_value[dataset.value] = len(filtered_scores[smallest_key])
#
#     import pdb
#
#     pdb.set_trace()
#
#     assert len(scores.filtered_by()) == 300
#     assert (
#         len(
#             scores.filtered_by(Filter(gender=Gender.FEMALE, dataset=Dataset.CASIA_FASD))
#         )
#         == 60
#     )
