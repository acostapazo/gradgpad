import copy
from typing import Dict

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn import metrics
import os
import random
import numpy as np

GENUINE_FLAG = 0


def det_curve(
    results_dict,
    path_to_save,
    title="DET Curve",
    genuine_label=0,
    subtypes: Dict[int, str] = None,
    colors: Dict[int, str] = None,
):
    """
    This function saves a static DET curve (FRR vs FAR)

    Parameters
    ----------
    results_dict: dict
        dict containing scores and labels
    path_to_save: str
        path where DET curve is saved
    title: str
        title of the plot
    genuine_label: int
        label that corresponds to the genuine class

    Returns
    -------

    """
    labels = copy.deepcopy(np.ravel(results_dict["labels"]))
    scores = copy.deepcopy(np.ravel(results_dict["scores"]))
    assert len(scores) == len(labels)

    plt.title(title)
    plt.ylim((0, 1))
    plt.xlim((0, 1))
    plt.xlabel("FAR")
    plt.ylabel("FRR")
    plt.grid(True)

    inv_scores = -1.0 * scores
    labels[labels == genuine_label] = 0
    handles = []

    if not subtypes:
        labels[labels != genuine_label] = 1
        far, tpr, _ = metrics.roc_curve(labels, inv_scores, pos_label=0)
        plt.plot(far, 1 - tpr)
    else:
        genuine_scores = inv_scores[labels == genuine_label]
        genuine_labels = labels[labels == genuine_label]
        for label in range(1, max(labels) + 1):
            type_pai_scores = inv_scores[labels == label]
            type_pai_labels = labels[labels == label]

            all_scores = np.concatenate((genuine_scores, type_pai_scores))
            all_labels = np.concatenate((genuine_labels, type_pai_labels))

            all_labels[all_labels == label] = 1

            far, tpr, _ = metrics.roc_curve(all_labels, all_scores, pos_label=0)

            color = colors.get(label) if colors else None
            subtype = subtypes.get(label)
            plt.plot(far, 1 - tpr, color=color)
            handles.append(mpatches.Patch(color=color, label=subtype))

        labels[labels != genuine_label] = 1
        far, tpr, _ = metrics.roc_curve(labels, inv_scores, pos_label=0)

        plt.plot(far, 1 - tpr, ls="--", color="b")
        handles.append(mpatches.Patch(color="b", label="All"))

    if handles:
        plt.legend(handles=handles)

    plt.savefig(path_to_save)
    plt.close()


def save_several_det_curves(dict_results, path_to_save):
    if not os.path.isdir(os.path.dirname(path_to_save)):
        raise IOError(
            "Output path [{}] does not exist".format(os.path.dirname(path_to_save))
        )

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xlabel("FAR")
    plt.ylabel("FRR")
    plt.grid(True)
    plt.ylim((0, 1))
    plt.xlim((0, 1))
    linewidth = 1.5

    lengend_labels = []
    for algorithm, results_dict in dict_results.items():

        if valid_labels(results_dict):
            lengend_labels.append(algorithm)
            scores = results_dict["scores"].ravel()
            labels = results_dict["labels"]
            labels = labels.ravel()
            labels[labels == GENUINE_FLAG] = 0
            labels[labels != GENUINE_FLAG] = 1

            assert len(scores) == len(labels)

            color, linestyle, marker = get_random_style()
            inv_scores = -1.0 * scores
            far, tpr, _ = metrics.roc_curve(labels, inv_scores, pos_label=0)
            ax.plot(
                far,
                1 - tpr,
                color=color,
                linestyle=linestyle,
                linewidth=linewidth,
                label=algorithm,
            )
        else:
            raise RuntimeError("Impossible to save a DET curve without labels")

    lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0)
    plt.savefig(path_to_save, bbox_extra_artists=(lgd,), bbox_inches="tight")


def valid_labels(results_dict):
    if "labels" in results_dict:
        if np.any(results_dict["labels"] is None):
            return False
        else:
            return True
    else:
        return False


def flatten_array(array):
    flat_labels_list = [item for sublist in array.tolist() for item in sublist]
    return np.array(flat_labels_list)


def get_random_style():
    colors = [
        "blue",
        "green",
        "red",
        "cyan",
        "magenta",
        "black",
        "brown",
        "chocolate",
        "fuchsia",
        "yellowgreen",
        "darkorange",
        "peru",
        "firebrick",
        "darkcyan",
        "lime",
        "gold",
        "olive",
        "royalblue",
        "teal",
        "violet",
        "darkviolet",
        "salmon",
        "bisque",
        "tan",
        "grey",
    ]
    linestyles = [":", "--", "-.", "-"]
    markers = [".", ",", "o", "v"]

    color_index = random.randint(0, len(colors) - 1)
    linestyle_index = random.randint(0, len(linestyles) - 1)
    markers_index = random.randint(0, len(markers) - 1)

    return colors[color_index], linestyles[linestyle_index], markers[markers_index]
