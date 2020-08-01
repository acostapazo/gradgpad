import pytest
import numpy as np

from gradgpad.evaluation.metrics.apcer_fixing_bpcer import apcer_fixing_bpcer

from gradgpad.reproducible_research import Scores


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores, labels, expected_apcer, apcer_working_point",
    [
        (
            np.array([0.1, 0.11, 0.6, 0.25, 0.0, 0.1, 0.2]),
            np.array([1, 1, 2, 2, 0, 0, 0]),
            0.5,  # 1.0,
            0.1,
        ),
        (
            np.array([0.1, 0.11, 0.6, 0.25, 0.0, 0.1, 0.2]),
            np.array([1, 1, 2, 2, 0, 0, 0]),
            0.25,  # 0.0,
            0.5,
        ),
        (
            np.array([0.1, 0.11, 0.6, 0.25, 0.0, 0.1, 0.2]),
            np.array([1, 1, 2, 2, 0, 0, 0]),
            0.25,  # 0.5,
            0.2,
        ),
        (
            np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]),
            np.array([1, 1, 2, 2, 0, 0, 0]),
            0.0,  # 1.0,
            0.5,
        ),
    ],
)
def test_should_compute_apcer_fixing_bpcer_correctly(
    scores, labels, expected_apcer, apcer_working_point
):
    apcer_fixing_bpcer_value = apcer_fixing_bpcer(scores, labels, apcer_working_point)
    assert expected_apcer == apcer_fixing_bpcer_value


@pytest.mark.unit
@pytest.mark.parametrize(
    "filename, expected_apcer, bpcer_working_point",
    [
        (
            "gradgpad/reproducible_research/scores/quality_rbf/quality_rbf_cross_dataset_csmad_test.json",
            1.0,  # 0.875,
            0.15,
        )
    ],
)
def test_should_compute_apcer_fixing_bpcer_correctly_from_filename(
    filename, expected_apcer, bpcer_working_point
):

    scores_gradgpad = Scores.from_filename(filename)

    scores = scores_gradgpad.get_numpy_scores()
    labels = scores_gradgpad.get_numpy_labels()

    apcer_fixing_apcer_value = apcer_fixing_bpcer(scores, labels, bpcer_working_point)

    assert expected_apcer == apcer_fixing_apcer_value


# from gradgpad.evaluation.plots.det_curve import det_curve
# from gradgpad.evaluation.plots.histogram import save_histogram
# from gradgpad.reproducible_research.scores.approach import Approach
# from gradgpad.reproducible_research.scores.protocol import Protocol
# from gradgpad.reproducible_research.scores.scores_provider import ScoresProvider
# from gradgpad.reproducible_research.scores.subset import Subset
# from gradgpad.annotations.coarse_grain_pai import CoarseGrainPai
# @pytest.mark.unit
# @pytest.mark.parametrize(
#     "expected_apcer, bpcer_working_point",
#     [
#         (
#             1.0,
#             0.1,
#         )
#     ],
# )
# def test_should_compute_apcer_fixing_bpcer_correctly_from_scores_provider(
#     expected_apcer, bpcer_working_point
# ):
#
#     scores_gradgpad = ScoresProvider.get(
#                 approach=Approach.QUALITY_RBF,
#                 protocol=Protocol.GRANDTEST,
#                 subset=Subset.TEST,
#             )
#
#     REPLAY_LOW_QUALITY_LABEL = 4
#     scores, labels = scores_gradgpad.get_numpy_scores_and_labels_filtered_by_labels([REPLAY_LOW_QUALITY_LABEL])
#
#
#     data = {"scores": scores, "labels": labels}
#
#     det_curve(data, "output/deleteme_aux_det.png")
#     save_histogram(
#         data,
#         "output/deleteme_aux_hist.png",
#         genuine_label=0,
#         normalize_hist=True
#     )
#     apcer_fixing_apcer_value = apcer_fixing_bpcer(scores, labels, bpcer_working_point)
#
#     assert pytest.approx(expected_apcer, 0.1) == apcer_fixing_apcer_value
