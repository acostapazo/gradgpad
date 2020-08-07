from gradgpad.evaluation.metrics.far import far


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

    apcer_value, th_apcer = far(scores, labels, bpcer_working_point)

    # Ad-hoc out-of-range detector
    # There is not chance to fix a working point from a given bpcer_working_point)
    if (apcer_value < 0.01) and (th_apcer > 0.99):
        apcer_value = 1.1

    return float(apcer_value)
