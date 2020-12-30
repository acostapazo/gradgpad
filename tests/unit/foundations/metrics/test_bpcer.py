import pytest
import numpy as np

from gradgpad.foundations.metrics.bpcer import bpcer

scores = np.array([0.0, 0.2, 0.2, 0.5, 0.6])
labels = np.array([1, 2, 2, 0, 0])
expected_bpcer = 1.0
th_eer_dev = 0.25


@pytest.mark.unit
def test_should_throw_an_exception_when_input_is_not_np_array():
    pytest.raises(TypeError, lambda: bpcer(scores.tolist(), labels, th_eer_dev))


@pytest.mark.unit
def test_should_compute_bpcer_correctly():
    bpcer_value = bpcer(scores, labels, th_eer_dev)
    assert pytest.approx(expected_bpcer, 0.1) == bpcer_value
