from gradgpad.foundations.metrics.apcer import apcer
from gradgpad.foundations.metrics.bpcer import bpcer


def acer(scores, labels, th_eer_dev):
    """
    Computes the Attack Classification Error Rate.

    Parameters
    ----------
    scores: np array
        It holds the score information for all samples (genuine and impostor).
        It is expected that impostor (negative) scores are, at least by design, greater than genuine (positive) scores.
    labels: np array
        It holds the labels (int). It is assumed that impostor_labels != 0 and genuine labels == 0
    th_eer_dev
        Equal Error Rate threshold at dev subset. Every impostor sample that falls bellow the threshold is considered a
        false-accept (FA). Genuine samples above the threshold are considered a false-rejection (FR).

    Returns
    -------

    """

    bpcer_value = bpcer(scores, labels, th_eer_dev)
    apcer_value = apcer(scores, labels, th_eer_dev)

    return (apcer_value + bpcer_value) / 2
