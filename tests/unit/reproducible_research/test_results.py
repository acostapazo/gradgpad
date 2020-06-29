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
