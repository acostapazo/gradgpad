import numpy as np


def apcer(scores, labels, th_eer_dev):
    """
    Computes the Attack Presentation Classification Error Rate.

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

    impostor_labels = labels[labels != 0]
    impostor_pais = np.unique(impostor_labels).tolist()

    pais_apcers = []
    for pai in impostor_pais:
        pai_scores = scores[labels == pai]
        pai_apcer = pai_scores[pai_scores < th_eer_dev].size / pai_scores.size
        pais_apcers.append(pai_apcer)

    apcer_value = max(pais_apcers)

    return apcer_value
