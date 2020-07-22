import pytest

from gradgpad.annotations.coarse_grain_pai import CoarseGrainPai
from gradgpad.annotations.dataset import Dataset
from gradgpad.annotations.device import Device
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.reproducible_research.scores.scores_provider import ScoresProvider
from gradgpad.reproducible_research.scores.subset import Subset


@pytest.mark.unit
@pytest.mark.parametrize(
    "approach,protocol,subset,expected_scores_length",
    [
        (approach, Protocol.GRANDTEST, subset, 12490 if subset == Subset.TEST else 4580)
        for approach in Approach.options()
        for subset in Subset.options()
        if approach != Approach.AUXILIARY  # pending
    ],
)
def test_should_success_get_scores_from_provider_grandtest_protocol_no_auxiliary(
    approach, protocol, subset, expected_scores_length
):

    scores = ScoresProvider.get(approach, protocol, subset)

    assert len(scores.scores) == expected_scores_length


@pytest.mark.unit
@pytest.mark.parametrize(
    "approach,protocol,subset,expected_scores_length",
    [
        (approach, Protocol.GRANDTEST, subset, 12533 if subset == Subset.TEST else 4585)
        for approach in Approach.options()
        for subset in Subset.options()
        if approach == Approach.AUXILIARY  # pending
    ],
)
def test_should_success_get_scores_from_provider_grandtest_protocol_auxiliary(
    approach, protocol, subset, expected_scores_length
):

    scores = ScoresProvider.get(approach, protocol, subset)

    assert len(scores.scores) == expected_scores_length


@pytest.mark.unit
@pytest.mark.parametrize(
    "approach,protocol,subset,dataset",
    [
        (approach, protocol, subset, dataset)
        for approach in Approach.options()
        for protocol in [Protocol.CROSS_DATASET, Protocol.LODO]
        for subset in Subset.options()
        for dataset in Dataset.options()
    ],
)
def test_should_success_get_scores_from_provider_cross_dataset_and_lodo_protocols(
    approach, protocol, subset, dataset
):
    scores = ScoresProvider.get(
        approach=approach, protocol=protocol, subset=subset, dataset=dataset
    )
    assert len(scores.scores) >= 0


@pytest.mark.unit
@pytest.mark.parametrize(
    "approach,protocol,subset,device",
    [
        (approach, Protocol.CROSS_DEVICE, subset, device)
        for approach in Approach.options()
        for subset in Subset.options()
        for device in Device.options()
    ],
)
def test_should_success_get_scores_from_provider_cross_device_protocol(
    approach, protocol, subset, device
):
    scores = ScoresProvider.get(
        approach=approach, protocol=protocol, subset=subset, device=device
    )
    assert len(scores.scores) >= 0


@pytest.mark.unit
@pytest.mark.parametrize(
    "approach,protocol,subset,pai",
    [
        (approach, Protocol.UNSEEN_ATTACK, subset, pai)
        for approach in Approach.options()
        for subset in Subset.options()
        for pai in CoarseGrainPai.options()
    ],
)
def test_should_success_get_scores_from_provider_unseen_attack_protocol(
    approach, protocol, subset, pai
):
    scores = ScoresProvider.get(
        approach=approach, protocol=protocol, subset=subset, pai=pai
    )
    assert len(scores.scores) >= 0


@pytest.mark.unit
@pytest.mark.parametrize(
    "approach,protocol,subset",
    [
        (approach, protocol, subset)
        for approach in Approach.options()
        for subset in Subset.options()
        for protocol in [
            Protocol.CROSS_DEVICE,
            Protocol.UNSEEN_ATTACK,
            Protocol.LODO,
            Protocol.CROSS_DATASET,
        ]
    ],
)
def test_should_throw_exception_get_scores_from_provider_unseen_attack_protocol(
    approach, protocol, subset
):
    with pytest.raises(ValueError) as excinfo:

        ScoresProvider.get(approach=approach, protocol=protocol, subset=subset)

    assert protocol.name.replace("_", "-") in str(excinfo.value)
