import sys

from gradgpad.public_api import GRADGPAD_SCORES_PATH
from gradgpad.foundations.annotations.coarse_grained_pai import CoarseGrainedPai
from gradgpad.foundations.annotations.dataset import Dataset
from gradgpad.foundations.annotations.device import Device
from gradgpad.reproducible_research import Scores
from gradgpad.foundations.scores.approach import Approach
from gradgpad.foundations.scores.protocol import Protocol
from gradgpad.foundations.scores.subset import Subset

sys.path.insert(0, GRADGPAD_SCORES_PATH)


def get_filename(
    approach: Approach,
    protocol: Protocol,
    subset: Subset,
    dataset: Dataset = None,
    device: Device = None,
    pai: CoarseGrainedPai = None,
):
    base_path = f"{GRADGPAD_SCORES_PATH}/{approach.value}"
    filename = f"{approach.value}_{protocol.value}"

    if (
        protocol == Protocol.CROSS_DATASET
        or protocol == Protocol.LODO
        or protocol == Protocol.INTRADATASET
    ):
        if not dataset:
            raise ValueError(
                f"{protocol.name} Protocol must be accompanied with a dataset value"
            )
        filename = f"{filename}_{dataset.value}"

    if protocol == Protocol.CROSS_DEVICE:
        if not device:
            raise ValueError(
                "CROSS-DEVICE Protocol must be accompanied with a device value"
            )
        filename = f"{filename}_{device.value}"

    if protocol == Protocol.UNSEEN_ATTACK:
        if not pai:
            raise ValueError(
                "UNSEEN-ATTACK Protocol must be accompanied with a pai value"
            )
        filename = f"{filename}_{pai.value}"

    filename = f"{filename}_{subset.value}.json".replace("-", "_")

    return f"{base_path}/{filename}"


class ScoresProvider:
    @staticmethod
    def all(approach: Approach):
        scores = {}
        for protocol in Protocol.options():
            if protocol == Protocol.GRANDTEST:
                key = protocol.value
                scores[key] = {}
                for subset in Subset.options():
                    scores[key][subset.value] = ScoresProvider.get(
                        approach=approach, protocol=protocol, subset=subset
                    )
            elif protocol == Protocol.CROSS_DATASET or protocol == Protocol.LODO:
                for dataset in Dataset.options():
                    key = f"{protocol.value}_{dataset.value}"
                    scores[key] = {}
                    for subset in Subset.options():
                        scores[key][subset.value] = ScoresProvider.get(
                            approach=approach,
                            protocol=protocol,
                            subset=subset,
                            dataset=dataset,
                        )
            elif protocol == Protocol.CROSS_DEVICE:
                for device in Device.options():
                    key = f"{protocol.value}_{device.value}"
                    scores[key] = {}
                    for subset in Subset.options():
                        scores[key][subset.value] = ScoresProvider.get(
                            approach=approach,
                            protocol=protocol,
                            subset=subset,
                            device=device,
                        )
            elif protocol == Protocol.UNSEEN_ATTACK:
                for pai in CoarseGrainedPai.options():
                    key = f"{protocol.value}_{pai.value}"
                    scores[key] = {}
                    for subset in Subset.options():
                        scores[key][subset.value] = ScoresProvider.get(
                            approach=approach, protocol=protocol, subset=subset, pai=pai
                        )
        return scores

    @staticmethod
    def get(
        approach: Approach,
        protocol: Protocol,
        subset: Subset,
        dataset: Dataset = None,
        device: Device = None,
        pai: CoarseGrainedPai = None,
    ) -> Scores:
        filename = get_filename(approach, protocol, subset, dataset, device, pai)
        return Scores.from_filename(filename)

    @staticmethod
    def get_subsets(approach: Approach, protocol: Protocol):
        return {
            subset.value: ScoresProvider.get(approach, protocol, subset)
            for subset in Subset.options()
        }
