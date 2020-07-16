import pytest
import numpy as np

from gradgpad.metrics.bpcer_fixing_apcer import bpcer_fixing_apcer


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores, labels, expected_bpcer, apcer_working_point",
    [
        (
            np.array([0.1, 0.11, 0.6, 0.25, 0.0, 0.1, 0.2]),
            np.array([1, 1, 2, 2, 0, 0, 0]),
            0.66,
            0.1,
        ),
        (
            np.array([0.1, 0.11, 0.6, 0.25, 0.0, 0.1, 0.2]),
            np.array([1, 1, 2, 2, 0, 0, 0]),
            0.33,
            0.5,
        ),
    ],
)
def test_should_compute_bpcer_fixing_apcer_correctly(
    scores, labels, expected_bpcer, apcer_working_point
):
    bpcer_fixing_apcer_value = bpcer_fixing_apcer(scores, labels, apcer_working_point)
    assert pytest.approx(expected_bpcer, 0.1) == bpcer_fixing_apcer_value


@pytest.mark.unit
@pytest.mark.parametrize(
    "filename, expected_apcer, apcer_working_point",
    [
        (
            "tests/resources/real_scores/cross-dataset-test-replay-mobile_scores_test.npy",
            1.0,  # TO
            0.15,
        )
    ],
)
def test_should_compute_bpcer_fixing_apcer_correctly_from_filename(
    filename, expected_apcer, apcer_working_point
):
    result = np.load(filename, allow_pickle=True).item()
    scores = result["scores"]
    labels = result["labels"]

    # from researchfellow import det_curve
    # det_curve(result, "deleteme.png")

    bpcer_fixing_apcer_value = bpcer_fixing_apcer(scores, labels, apcer_working_point)

    import pdb

    pdb.set_trace()
    assert bpcer_fixing_apcer_value <= 1.0
