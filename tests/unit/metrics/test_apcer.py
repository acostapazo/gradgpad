import pytest
import numpy as np

# scores = np.array([0.5, 0.6, 0.2, 0.0, 0.0])
# labels = np.array([1, 2, 2, 0, 0])
# expected_apcer = 0.0
# th_eer_dev = 0.15
from gradgpad.metrics.apcer import apcer


@pytest.mark.unit
def test_should_throw_an_exception_when_input_is_not_np_array():
    pytest.raises(
        TypeError, lambda: apcer([0.5, 0.6, 0.2, 0.0, 0.0], [1, 2, 2, 0, 0], 0.15)
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores, labels, expected_apcer, th_eer",
    [
        (np.array([0.5, 0.6, 0.2, 0.0, 0.0]), np.array([1, 2, 2, 0, 0]), 0.0, 0.15),
        (np.array([0.1, 0.6, 0.2, 0.0, 0.0]), np.array([1, 2, 2, 0, 0]), 1.0, 0.15),
    ],
)
def test_should_compute_apcer_correctly(scores, labels, expected_apcer, th_eer):
    apcer_value = apcer(scores, labels, th_eer)
    assert pytest.approx(expected_apcer, 0.1) == apcer_value
