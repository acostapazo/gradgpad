import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import warnings

warnings.filterwarnings("ignore", module="matplotlib")


def valid_labels(results_dict):
    if "labels" in results_dict:
        if np.any(results_dict["labels"] == None):  # noqa
            return False
        else:
            return True
    else:
        return False


def save_histogram(
    results_dict,
    filename_result_histogram,
    genuine_label=0,
    th=None,
    th_legend="",
    normalize_hist=False,
    y_lim=None,
    title="Histogram",
):
    """
    This function saves a static histogram

    Parameters
    ----------
    results_dict: dict
        dict containing scores and labels
    filename_result_histogram: str
        full path where the histogram is saved
    genuine_label: int
        label that corresponds to the genuine class
    th: float
        threshold to display
    th_legend: str
        threshold legend
    normalize_hist: boolean
        determines whether it normalizes the hist
    y_lim: float
        y axis max

    Returns
    -------

    """

    if not os.path.isdir(os.path.dirname(filename_result_histogram)):
        raise IOError(
            "Output path [{}] does not exist".format(
                os.path.dirname(filename_result_histogram)
            )
        )

    scores = results_dict["scores"]

    plt.figure()
    plt.xlabel("Score")
    plt.ylabel("Count")
    plt.title(title)

    if valid_labels(results_dict):

        labels = results_dict["labels"].ravel()
        assert len(scores) == len(labels)

        genuine = scores[labels == genuine_label]
        impostors = scores[labels != genuine_label]

        hist_gen, edges_gen = np.histogram(genuine, bins=50)
        hist_impos, edges_impos = np.histogram(impostors, bins=50)

        if normalize_hist:
            hist_gen = hist_gen / hist_gen.max()
            hist_impos = hist_impos / hist_impos.max()

        if y_lim:
            axes = plt.gca()
            axes.set_ylim([0, y_lim])

        max_value = max(hist_gen.max(), hist_impos.max())

        plt.bar(
            (edges_gen[1:] + edges_gen[:-1]) * 0.5,
            hist_gen,
            width=(edges_gen[1] - edges_gen[0]),
            facecolor="g",
            alpha=0.5,
        )

        plt.bar(
            (edges_impos[1:] + edges_impos[:-1]) * 0.5,
            hist_impos,
            width=(edges_impos[1] - edges_impos[0]),
            facecolor="r",
            alpha=0.5,
        )

        red_patch = mpatches.Patch(
            color="red", label="Impostors ({})".format(len(impostors))
        )
        green_patch = mpatches.Patch(
            color="green", label="Genuine ({})".format(len(genuine))
        )

        if th is not None:
            x, y = [th, th], [0, max_value]
            th_line, = plt.plot(x, y, "b--", label=th_legend)
            plt.legend(handles=[red_patch, green_patch, th_line])
        else:
            plt.legend(handles=[red_patch, green_patch])

    else:
        hist, edges = np.histogram(scores, bins=50)

        if normalize_hist:
            hist = hist / hist.max()

        max_value = hist.max()

        plt.bar(
            (edges[1:] + edges[:-1]) * 0.5,
            hist,
            width=(edges[1] - edges[0]),
            facecolor="m",
            alpha=0.5,
        )
        patch = mpatches.Patch(color="m", label="Samples ({})".format(len(scores)))

        if th is not None:
            x, y = [th, th], [0, max_value]
            th_line, = plt.plot(x, y, "b--", label=th_legend)
            plt.legend(handles=[patch, th_line])
        else:
            plt.legend(handles=[patch])

    plt.savefig(filename_result_histogram)
    plt.close("all")
