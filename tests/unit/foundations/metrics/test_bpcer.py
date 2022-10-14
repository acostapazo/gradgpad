import numpy as np
import pytest

from gradgpad.foundations.metrics.bpcer import bpcer

scores = np.array([0.0, 0.2, 0.2, 0.5, 0.6])
labels = np.array([1, 2, 2, 0, 0])
expected_bpcer = 1.0
th_eer_dev = 0.25


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores, labels",
    [
        (scores.tolist(), labels),
        (scores, labels.tolist()),
        (scores.tolist(), labels.tolist()),
    ],
)
def test_should_throw_an_exception_when_input_is_not_np_array(scores, labels):
    pytest.raises(TypeError, lambda: bpcer(scores, labels, 0.15))


@pytest.mark.unit
def test_should_compute_bpcer_correctly():
    bpcer_value = bpcer(scores, labels, th_eer_dev)
    assert pytest.approx(expected_bpcer, 0.1) == bpcer_value
