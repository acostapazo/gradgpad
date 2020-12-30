import pytest
import numpy as np

from gradgpad.foundations.metrics.hter import hter

scores = np.array([0.0, 0.2, 0.2, 0.5, 0.6])
labels = np.array([1, 2, 2, 0, 0])
expected_hter = 0.66
th_eer_dev = 0.25


@pytest.mark.unit
def test_should_throw_an_exception_when_input_is_not_np_array():
    pytest.raises(TypeError, lambda: hter(scores.tolist(), labels, th_eer_dev))


@pytest.mark.unit
def test_should_compute_hter_correctly():
    hter_value = hter(scores, labels, th_eer_dev)
    assert pytest.approx(expected_hter, 0.66) == hter_value
