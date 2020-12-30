import numpy as np
from sklearn import metrics


def frr(scores, labels, far_op):

    """
    Calculates FRR from FAR operating point.

    Parameters
    ----------
    scores: np array
        It holds the score information for all samples (genuine and impostor).
        It is expected that impostor (negative) scores are, at least by design, greater than genuine (positive) scores.
    labels: np array
        It holds the labels (int). It is assumed that impostor_labels != 0 and genuine labels == 0
    far_op: float
        Closest FAR value to look for.

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

    frr, th = _frr_from_far_value(fars, tprs, ths, far_op)

    return frr, th


def _frr_from_far_value(fars, tprs, ths, far_op):
    idx_far = (np.abs(fars - far_op)).argmin()
    th = ths[idx_far]
    frr = 1 - tprs[idx_far]

    return frr, th
