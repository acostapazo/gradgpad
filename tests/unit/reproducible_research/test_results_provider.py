import pytest

from gradgpad.reproducible_research.results.results_provider import ResultsProvider
from gradgpad.reproducible_research.scores.approach import Approach


@pytest.fixture
def expected_protocols():
    return [
        "grandtest",
        "cross_dataset_casia-fasd",
        "cross_dataset_threedmad",
        "cross_dataset_uvad",
        "cross_dataset_siw-m",
        "cross_dataset_siw",
        "cross_dataset_rose-youtu",
        "cross_dataset_replay-mobile",
        "cross_dataset_replay-attack",
        "cross_dataset_oulu-npu",
        "cross_dataset_msu-mfsd",
        "cross_dataset_hkbuV2",
        "cross_dataset_hkbu",
        "cross_dataset_csmad",
        "cross_device_digital_camera",
        "cross_device_mobile_tablet",
        "cross_device_webcam",
        "lodo_casia-fasd",
        "lodo_threedmad",
        "lodo_uvad",
        "lodo_siw-m",
        "lodo_siw",
        "lodo_rose-youtu",
        "lodo_replay-mobile",
        "lodo_replay-attack",
        "lodo_oulu-npu",
        "lodo_msu-mfsd",
        "lodo_hkbuV2",
        "lodo_hkbu",
        "lodo_csmad",
        "unseen_attack_print",
        "unseen_attack_replay",
        "unseen_attack_mask",
        "unseen_attack_makeup",
        "unseen_attack_partial",
    ]


@pytest.mark.unit
@pytest.mark.parametrize(
    "approach", Approach.options_excluding([Approach.CONTINUAL_LEARNING_AUXILIARY])
)
def test_should_success_provide_results(approach: Approach, expected_protocols):

    results = ResultsProvider.all(approach)
    assert len(results.keys()) == 35
    assert sorted(results.keys()) == sorted(expected_protocols)
