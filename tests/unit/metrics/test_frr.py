import pytest
import numpy as np

from gradgpad.evaluation.metrics.frr import frr

scores = np.array([0.0, 0.2, 0.2, 0.5, 0.6])
labels = np.array([1, 2, 2, 0, 0])
far_op = 0.1
expected_frr = 1.0


@pytest.mark.unit
def test_should_throw_an_exception_when_input_is_not_np_array():
    pytest.raises(TypeError, lambda: frr(scores.tolist(), labels, far_op))


@pytest.mark.unit
def test_should_compute_frr_correctly():
    frr_value, th = frr(scores, labels, far_op)
    assert pytest.approx(expected_frr, 0.1) == frr_value
