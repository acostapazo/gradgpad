import numpy as np
import pytest

from gradgpad.foundations.metrics.far import far

scores = np.array([0.0, 0.2, 0.2, 0.5, 0.6])
labels = np.array([1, 2, 2, 0, 0])
frr_op = 0.1
expected_far = 1.0


@pytest.mark.unit
def test_should_throw_an_exception_when_input_is_not_np_array():
    pytest.raises(TypeError, lambda: far(scores.tolist(), labels, frr_op))


@pytest.mark.unit
def test_should_compute_far_correctly():
    far_value, th = far(scores, labels, frr_op)
    assert pytest.approx(expected_far, 0.1) == far_value
