import numpy as np


def bpcer(scores, labels, th_eer_dev):
    """
    Computes the Bonafide Presentation Classification Error Rate.

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

    assert len(scores) == len(labels)

    genuine_score = scores[labels == 0]
    bpcer = genuine_score[genuine_score > th_eer_dev].size / genuine_score.size

    return bpcer
