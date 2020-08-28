import numpy as np
from sklearn import metrics
from scipy.optimize import brentq
from scipy.interpolate import interp1d


def eer(scores, labels):
    """
    Computes Equal Error Rate.

    Parameters
    ----------
    scores: np array
        It holds the score information for all samples (genuine and impostor).
        It is expected that impostor (negative) scores are, at least by design, greater than genuine (positive) scores.
    labels: np array
        It holds the labels (int). It is assumed that impostor_labels != 0 and genuine labels == 0

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

    eer = brentq(lambda x: 1.0 - x - interp1d(fars, tprs)(x), 0.0, 1.0)
    eer_th = interp1d(fars, ths, kind="slinear")(eer)

    return eer, eer_th
