import os


from gradgpad.annotations.coarse_grain_pai import CoarseGrainPai
from gradgpad.annotations.dataset import Dataset
from gradgpad.annotations.device import Device
from gradgpad.reproducible_research import Scores
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.reproducible_research.scores.subset import Subset


REPRODUCIBLE_RESEARCH_SCORES_DIR = os.path.abspath(os.path.dirname(__file__))


def get_filename(
    approach: Approach,
    protocol: Protocol,
    subset: Subset,
    dataset: Dataset = None,
    device: Device = None,
    pai: CoarseGrainPai = None,
):

    filename = f"{REPRODUCIBLE_RESEARCH_SCORES_DIR}/{approach.value}/{approach.value}"

    if protocol == Protocol.LODO:
        if not dataset:
            raise ValueError("LODO Protocol must be accompanied with a dataset value")
        filename = f"{filename}_{dataset.value}_{protocol.value}"
    else:
        filename = f"{filename}_{protocol.value}"

        if protocol == Protocol.CROSS_DATASET:
            if not dataset:
                raise ValueError(
                    "CROSS-DATASET Protocol must be accompanied with a dataset value"
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

    return f"{filename}_{subset.value}.json".replace("-", "_")


class ScoresProvider:
    @staticmethod
    def get(
        approach: Approach,
        protocol: Protocol,
        subset: Subset,
        dataset: Dataset = None,
        device: Device = None,
        pai: CoarseGrainPai = None,
    ) -> Scores:
        filename = get_filename(approach, protocol, subset, dataset, device, pai)

        return Scores(filename)
