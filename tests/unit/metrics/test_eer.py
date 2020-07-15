import pytest
import numpy as np
from gradgpad.metrics.eer import eer
from gradgpad.reproducible_research import quality_linear_scores_grandtest_type_I_test

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

    eer_value, th = eer(
        quality_linear_scores_grandtest_type_I_test.get_numpy_scores(),
        quality_linear_scores_grandtest_type_I_test.get_numpy_labels(),
    )
    assert pytest.approx(expected_eer, 0.1) == 0.24
