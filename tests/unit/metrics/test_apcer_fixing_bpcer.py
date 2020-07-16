import pytest
import numpy as np

from gradgpad.metrics.apcer_fixing_bpcer import apcer_fixing_bpcer


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores, labels, expected_apcer, apcer_working_point",
    [
        (
            np.array([0.1, 0.11, 0.6, 0.25, 0.0, 0.1, 0.2]),
            np.array([1, 1, 2, 2, 0, 0, 0]),
            1.0,
            0.1,
        ),
        (
            np.array([0.1, 0.11, 0.6, 0.25, 0.0, 0.1, 0.2]),
            np.array([1, 1, 2, 2, 0, 0, 0]),
            0.0,
            0.5,
        ),
        (
            np.array([0.1, 0.11, 0.6, 0.25, 0.0, 0.1, 0.2]),
            np.array([1, 1, 2, 2, 0, 0, 0]),
            0.5,
            0.2,
        ),
    ],
)
def test_should_compute_apcer_fixing_bpcer_correctly(
    scores, labels, expected_apcer, apcer_working_point
):
    apcer_fixing_apcer_value = apcer_fixing_bpcer(scores, labels, apcer_working_point)
    assert pytest.approx(expected_apcer, 0.1) == apcer_fixing_apcer_value


# @pytest.mark.unit
# @pytest.mark.parametrize(
#     "filename, expected_apcer, bpcer_working_point",
#     [
#         (
#             "tests/resources/real_scores/cross-dataset-test-replay-mobile_scores_test.npy",
#             1.0, # TO
#             0.15,
#         )
#     ],
# )
# def test_should_compute_apcer_fixing_bpcer_correctly_from_filename(
#     filename, expected_apcer, bpcer_working_point
# ):
#     result = np.load(filename, allow_pickle=True).item()
#     scores = result["scores"]
#     labels = result["labels"]
#
#     #from researchfellow import det_curve
#     #det_curve(result, "deleteme.png")
#
#     apcer_fixing_apcer_value = apcer_fixing_bpcer(scores, labels, bpcer_working_point)
#
#     assert apcer_fixing_apcer_value <= 1.0
#     # assert pytest.approx(expected_apcer, 0.1) == apcer_fixing_apcer_value
