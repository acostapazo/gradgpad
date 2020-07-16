import numpy as np
from sklearn import metrics


def far(scores, labels, frr_op):

    """
    Calculates FAR from FRR operating point.

    Parameters
    ----------
    scores: np array
        It holds the score information for all samples (genuine and impostor).
        It is expected that impostor (negative) scores are, at least by design, greater than genuine (positive) scores.
    labels: np array
        It holds the labels (int). It is assumed that impostor_labels != 0 and genuine labels == 0
    frr_op: float
        Closest FRR value to look for.

    Returns
    -------

    """
    if not isinstance(scores, np.ndarray) or not isinstance(scores, np.ndarray):
        raise TypeError(
            "Scores [{}] and labels [{}] must be numpy arrays.".format(
                type(scores), type(labels)
            )
        )

    scores = scores.ravel()
    labels = labels.ravel()

    inlabels = np.zeros_like(labels)
    inlabels[labels != 0] = 1

    assert len(scores) == len(inlabels)

    inv_scores = -1.0 * scores
    fars, tprs, ths = metrics.roc_curve(inlabels, inv_scores, pos_label=0)
    ths = -1.0 * ths
    ths = np.clip(ths, scores.min(), scores.max())

    far, th = _far_from_frr_value(fars, tprs, ths, frr_op)

    return far, th


def _far_from_frr_value(fars, tprs, ths, frr_op):
    frrs = 1 - tprs
    idx_frr = (np.abs(frrs - frr_op)).argmin()
    th = ths[idx_frr]
    far = fars[idx_frr]

    return far, th
