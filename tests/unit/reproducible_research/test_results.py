import pytest


@pytest.mark.unit
def test_should_load_quality_results():
    from gradgpad.reproducible_research import quality_results

    assert len(quality_results.keys()) >= 50


@pytest.mark.unit
def test_should_load_quality_results_gender():
    from gradgpad.reproducible_research import quality_results_gender

    assert len(quality_results_gender.keys()) == 2


@pytest.mark.unit
def test_should_load_quality_results_skin_tone():
    from gradgpad.reproducible_research import quality_results_skin_tone

    assert len(quality_results_skin_tone.keys()) == 6


@pytest.mark.unit
def test_should_load_quality_results_age():
    from gradgpad.reproducible_research import quality_results_age

    assert len(quality_results_age.keys()) == 3


@pytest.mark.unit
def test_should_load_quality_results_cross_dataset():
    from gradgpad.reproducible_research import quality_results_cross_dataset

    assert len(quality_results_cross_dataset.keys()) == 13


@pytest.mark.unit
def test_should_load_quality_results_lodo():
    from gradgpad.reproducible_research import quality_results_lodo

    assert len(quality_results_lodo.keys()) == 13


@pytest.mark.unit
def test_should_load_quality_results_cross_device():
    from gradgpad.reproducible_research import quality_results_cross_device

    assert len(quality_results_cross_device.keys()) == 3


@pytest.mark.unit
def test_should_load_quality_results_unseen_attack():
    from gradgpad.reproducible_research import quality_results_unseen_attack

    assert len(quality_results_unseen_attack.keys()) == 5


# @pytest.mark.unit
# def test_should_load_auxiliary_results():
#     from gradgpad.reproducible_research import auxiliary_results
#
#     assert len(auxiliary_results.keys()) >= 50


@pytest.mark.unit
def test_should_load_auxiliary_results_gender():
    from gradgpad.reproducible_research import auxiliary_results_gender

    assert len(auxiliary_results_gender.keys()) == 2


@pytest.mark.unit
def test_should_load_auxiliary_results_skin_tone():
    from gradgpad.reproducible_research import auxiliary_results_skin_tone

    assert len(auxiliary_results_skin_tone.keys()) == 6


@pytest.mark.unit
def test_should_load_auxiliary_results_age():
    from gradgpad.reproducible_research import auxiliary_results_age

    assert len(auxiliary_results_age.keys()) == 3


@pytest.mark.unit
def test_should_load_auxiliary_results_cross_dataset():
    from gradgpad.reproducible_research import auxiliary_results_cross_dataset

    assert len(auxiliary_results_cross_dataset.keys()) == 13


@pytest.mark.unit
def test_should_load_auxiliary_results_lodo():
    from gradgpad.reproducible_research import auxiliary_results_lodo

    assert len(auxiliary_results_lodo.keys()) == 13


@pytest.mark.unit
def test_should_load_auxiliary_results_cross_device():
    from gradgpad.reproducible_research import auxiliary_results_cross_device

    assert len(auxiliary_results_cross_device.keys()) == 3


# @pytest.mark.unit
# def test_should_load_auxiliary_results_unseen_attack():
#     from gradgpad.reproducible_research import auxiliary_results_unseen_attack
#
#     assert len(auxiliary_results_unseen_attack.keys()) == 5


@pytest.mark.unit
def test_should_load_quality_linear_results():
    from gradgpad.reproducible_research import quality_linear_results

    assert len(quality_linear_results.keys()) >= 50


@pytest.mark.unit
def test_should_load_quality_linear_results_gender():
    from gradgpad.reproducible_research import quality_linear_results_gender

    assert len(quality_linear_results_gender.keys()) == 2


@pytest.mark.unit
def test_should_load_quality_linear_results_skin_tone():
    from gradgpad.reproducible_research import quality_linear_results_skin_tone

    assert len(quality_linear_results_skin_tone.keys()) == 6


@pytest.mark.unit
def test_should_load_quality_linear_results_age():
    from gradgpad.reproducible_research import quality_linear_results_age

    assert len(quality_linear_results_age.keys()) == 3


@pytest.mark.unit
def test_should_load_quality_linear_results_cross_dataset():
    from gradgpad.reproducible_research import quality_linear_results_cross_dataset

    assert len(quality_linear_results_cross_dataset.keys()) == 13


@pytest.mark.unit
def test_should_load_quality_linear_results_lodo():
    from gradgpad.reproducible_research import quality_linear_results_lodo

    assert len(quality_linear_results_lodo.keys()) == 13


@pytest.mark.unit
def test_should_load_quality_linear_results_cross_device():
    from gradgpad.reproducible_research import quality_linear_results_cross_device

    assert len(quality_linear_results_cross_device.keys()) == 3


@pytest.mark.unit
def test_should_load_quality_linear_results_unseen_attack():
    from gradgpad.reproducible_research import quality_linear_results_unseen_attack

    assert len(quality_linear_results_unseen_attack.keys()) == 5
