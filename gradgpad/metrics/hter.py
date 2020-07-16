import numpy as np
from sklearn import metrics


def hter(scores, labels, th_eer_dev):
    """
    Computes the Half Total Error Rate.

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

    hter = _hter_from_th_eer_dev(fars, tprs, ths, th_eer_dev)

    return hter


def _hter_from_th_eer_dev(fars, tprs, ths, th_eer_dev):
    idx_th = (np.abs(ths - th_eer_dev)).argmin()
    far = fars[idx_th]
    frr = 1 - tprs[idx_th]
    hter = (far + frr) / 2

    return hter
