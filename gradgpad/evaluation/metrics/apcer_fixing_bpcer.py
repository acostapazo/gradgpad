import numpy as np

from gradgpad.evaluation.metrics.apcer import apcer
from gradgpad.evaluation.metrics.bpcer import bpcer
from gradgpad.evaluation.metrics.get_target_value_fixing_working_point import (
    get_target_value_fixing_working_point,
)


def apcer_fixing_bpcer(scores, labels, bpcer_working_point):
    """
    Computes the Attack Presentation Classification Error Rate.

    Parameters
    ----------
    scores: np array
        It holds the score information for all samples (genuine and impostor).
        It is expected that impostor (negative) scores are, at least by design, greater than genuine (positive) scores.
    labels: np array
        It holds the labels (int). It is assumed that impostor_labels != 0 and genuine labels == 0
    bpcer_working_point
        Fixing APCER from BPCER working point

    Returns
    -------

    """
    possible_apcers = []
    possible_bpcers = []
    thresholds = []
    for th in np.linspace(scores.min(), scores.max(), 100):
        possible_apcers.append(apcer(scores, labels, th))
        possible_bpcers.append(bpcer(scores, labels, th))
        thresholds.append(th)

    apcer_value, bpcer_value, threshold_value = get_target_value_fixing_working_point(
        bpcer_working_point,
        possible_bpcers,
        possible_apcers,
        thresholds,
        interpolated=True,
    )

    return bpcer_value
