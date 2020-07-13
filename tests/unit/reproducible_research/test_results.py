import pytest


@pytest.fixture
def expected_protocols():
    return [
        "Age - Adult",
        "Age - Senior",
        "Age - Young",
        "Cross-Dataset - 3DMAD",
        "Cross-Dataset - CASIA-FASD",
        "Cross-Dataset - CSMAD",
        "Cross-Dataset - HKBU",
        "Cross-Dataset - HKBU V2",
        "Cross-Dataset - MSU-MFSD",
        "Cross-Dataset - Oulu-NPU",
        "Cross-Dataset - Replay-Attack",
        "Cross-Dataset - Replay-Mobile",
        "Cross-Dataset - Rose-Youtu",
        "Cross-Dataset - SiW",
        "Cross-Dataset - SiW-M",
        "Cross-Dataset - UVAD",
        "Cross-Device - Digital Camera",
        "Cross-Device - Mobile|Tablet",
        "Cross-Device - Webcam",
        "Gender - Female",
        "Gender - Male",
        "Grandtest-Train-Type-PAI-I-Test-All",
        "Grandtest-Type-PAI-I",
        "LODO - 3DMAD",
        "LODO - CASIA-FASD",
        "LODO - CSMAD",
        "LODO - HKBU",
        "LODO - HKBU V2",
        "LODO - MSU-MFSD",
        "LODO - Oulu-NPU",
        "LODO - Replay-Attack",
        "LODO - Replay-Mobile",
        "LODO - Rose-Youtu",
        "LODO - SiW",
        "LODO - SiW-M",
        "LODO - UVAD",
        "Skin Tone - Dark Brown",
        "Skin Tone - Light Pink",
        "Skin Tone - Light Yellow",
        "Skin Tone - Medium Dark Brown",
        "Skin Tone - Medium Pink Brown",
        "Skin Tone - Medium Yellow Brown",
        "Unseen-Attack - Makeup",
        "Unseen-Attack - Mask",
        "Unseen-Attack - Partial",
        "Unseen-Attack - Print",
        "Unseen-Attack - Replay",
        "age-bias-grad-gpad-all",
        "gender-bias-grad-gpad-all",
        "skin-tone-bias-grad-gpad-all",
    ]


@pytest.mark.unit
def test_should_load_quality_results(expected_protocols):
    from gradgpad.reproducible_research import quality_results

    assert len(quality_results.keys()) >= 50
    assert sorted(quality_results.keys()) == expected_protocols


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


@pytest.mark.unit
def test_should_load_auxiliary_results(expected_protocols):
    from gradgpad.reproducible_research import auxiliary_results

    assert len(auxiliary_results.keys()) >= 50
    assert sorted(auxiliary_results.keys()) == expected_protocols


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


@pytest.mark.unit
def test_should_load_auxiliary_results_unseen_attack():
    from gradgpad.reproducible_research import auxiliary_results_unseen_attack

    assert len(auxiliary_results_unseen_attack.keys()) == 5


@pytest.mark.unit
def test_should_load_quality_linear_results(expected_protocols):
    from gradgpad.reproducible_research import quality_linear_results

    assert len(quality_linear_results.keys()) >= 50
    assert sorted(quality_linear_results.keys()) == expected_protocols


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
