import os

from gradgpad import public_api
from gradgpad.annotations.annotations import annotations  # noqa
from gradgpad.annotations.stats.calculate_pai_stats import calculate_pai_stats  # noqa
from gradgpad.annotations.dataset import Dataset  # noqa
from gradgpad.annotations.filter import Filter  # noqa
from gradgpad.annotations.device import Device  # noqa
from gradgpad.annotations.coarse_grain_pai import CoarseGrainPai  # noqa
from gradgpad.annotations.scenario import Scenario  # noqa
from gradgpad.annotations.person_attributes import Sex, Age, SkinTone  # noqa
from gradgpad.reproducible_research.scores.approach import Approach  # noqa
from gradgpad.reproducible_research.scores.protocol import Protocol  # noqa
from gradgpad.reproducible_research.scores.scores_provider import ScoresProvider  # noqa
from gradgpad.reproducible_research.scores.subset import Subset  # noqa

GRADGPAD_PATH = os.path.abspath(os.path.dirname(__file__))
GRADGPAD_SCORES_PATH = f"{GRADGPAD_PATH}/reproducible_research/scores/"

os.environ["GRADGPAD_PATH"] = GRADGPAD_PATH
os.environ["GRADGPAD_SCORES_PATH"] = GRADGPAD_SCORES_PATH


__all__ = public_api.__all__
