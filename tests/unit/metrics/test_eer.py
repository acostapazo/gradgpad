import pytest
import numpy as np
from gradgpad.evaluation.metrics.eer import eer
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.reproducible_research.scores.scores_provider import ScoresProvider
from gradgpad.reproducible_research.scores.subset import Subset

scores = np.array([0.0, 0.2, 0.2, 0.5, 0.6])
labels = np.array([1, 2, 2, 0, 0])
expected_eer = 0.99


@pytest.mark.unit
def test_should_throw_an_exception_when_input_is_not_np_array():
    pytest.raises(TypeError, lambda: eer(scores.tolist(), labels))


@pytest.mark.unit
def test_should_compute_eer_correctly():
    eer_value, th = eer(scores, labels)
    assert pytest.approx(expected_eer, 0.1) == eer_value


@pytest.mark.unit
def test_should_compute_eer_correctly_from_scores():
    scores = ScoresProvider.get(
        approach=Approach.QUALITY_LINEAR,
        protocol=Protocol.GRANDTEST,
        subset=Subset.DEVEL,
    )
    eer_value, th = eer(scores.get_numpy_scores(), scores.get_numpy_labels())
    assert pytest.approx(eer_value, 0.01) == 0.269
