import numpy as np

from gradgpad.foundations.metrics.far import far


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
    if len(np.unique(labels)) < 3:
        apcer_value, th_apcer = far(scores, labels, bpcer_working_point)
    else:
        apcer_values = []
        for label in np.unique(labels):
            if label == 0:
                continue

            genuine_scores = scores[labels == 0]
            impostor_scores = scores[labels == label]

            genuine_labels = labels[labels == 0]
            impostor_labels = labels[labels == label]

            filtered_scores = np.concatenate((genuine_scores, impostor_scores))
            filtered_labels = np.concatenate((genuine_labels, impostor_labels))

            apcer_value, th_apcer = far(
                filtered_scores, filtered_labels, bpcer_working_point
            )
            if apcer_value > 1.0:  # out of range:
                continue

            apcer_values.append(apcer_value)
        apcer_value = max(apcer_values)

    # TODO REVIEW
    # data = {
    #     "scores": scores,
    #     "labels": labels,
    # }
    # if apcer_value < 0.08:
    #     # print(f"{apcer_value} ({th_apcer})")
    #     # print(min(scores[labels==1]))
    #
    #     import time
    #     timestr = time.strftime("%Y%m%d-%H%M%S")
    #
    #     output_det_filename = f"deleteme/{timestr}_det.png"
    #     from gradgpad.evaluation.plots.det_curve import det_curve
    #     det_curve(data, output_det_filename)
    #
    #     output_hist_filename = f"deleteme/{timestr}_hist.png"
    #     from gradgpad.evaluation.plots.histogram import save_histogram
    #     save_histogram(
    #                         data,
    #                         output_hist_filename,
    #                         genuine_label=0,
    #                         th=th_apcer,
    #                         th_legend="Th APCER",
    #                         normalize_hist=True,
    #                     )

    return float(apcer_value)
