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
    apcer_value, _ = far(scores, labels, bpcer_working_point)

    return float(apcer_value)
