from gradgpad.foundations.metrics.frr import frr


def bpcer_fixing_apcer(scores, labels, apcer_working_point):
    """
    Computes the Attack Presentation Classification Error Rate.

    Parameters
    ----------
    scores: np array
        It holds the score information for all samples (genuine and impostor).
        It is expected that impostor (negative) scores are, at least by design, greater than genuine (positive) scores.
    labels: np array
        It holds the labels (int). It is assumed that impostor_labels != 0 and genuine labels == 0
    apcer_working_point
        Fixing BPCER from APCER working point

    Returns
    -------

    """

    bpcer_value, _ = frr(scores, labels, apcer_working_point)
    return float(bpcer_value)
