import os
from typing import Tuple

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import warnings
from sklearn import metrics

from gradgpad.foundations.scores import Scores, List
from gradgpad.tools.visualization.colors import get_color_random_style
from gradgpad.tools.visualization.histogram.split_by_level_mode import SplitByLabelMode
from gradgpad.tools.visualization.interface_plotter import IPlotter
from gradgpad.tools.visualization.scores_and_labels_formatter import (
    ScoresAndLabelsFormatter,
)

warnings.filterwarnings("ignore", module="matplotlib")


class DetPlotter(IPlotter):
    def __init__(
        self,
        title="DET",
        split_by_label_mode: SplitByLabelMode = SplitByLabelMode.NONE,
        genuine_label: int = 0,
        exclude_labels: List[int] = None,
        figsize: Tuple = (8, 8),
    ):
        """
        Parameters
        ----------
        title: str
            Title of the figure
        split_by_label_mode: SplitByLabelMode
            Select the way of subdivision of labels
        genuine_label: int
            label that corresponds to the genuine class
        exclude_labels: list
            List of excluded labels
        figsize: Tupla
            size of the figure
        """
        self.title = title

        if split_by_label_mode not in SplitByLabelMode.options_for_curves():
            raise TypeError(
                f"Det only accept the following SplitByLabelMode options: {SplitByLabelMode.options_for_curves()}"
            )
        self.split_by_label_mode = split_by_label_mode
        self.split_labels_correspondences = None
        self.genuine_label = genuine_label
        self.exclude_labels = exclude_labels
        self.figsize = figsize

    def _plot_curve(
        self, plt, scores, labels, label_correspondence="All", suffix_label=""
    ):
        far, tpr, _ = metrics.roc_curve(labels, scores, pos_label=0)

        color, linestyle, marker = get_color_random_style()

        linewidth = 1.5
        plt.plot(
            far,
            1 - tpr,
            color=color,
            linestyle=linestyle,
            linewidth=linewidth,
            label=label_correspondence,
        )

        patch = mpatches.Patch(
            color=color,
            linestyle=linestyle,
            linewidth=linewidth,
            label=f"{label_correspondence}{suffix_label}",
        )
        return patch

    def _calculate_det_curve(self, np_scores, np_labels):

        plt.figure(figsize=self.figsize)
        plt.title(self.title)
        plt.ylim((0, 1))
        plt.xlim((0, 1))
        plt.xlabel("FAR")
        plt.ylabel("FRR")
        plt.grid(True)

        np_scores = -1.0 * np_scores
        assert len(np_scores) == len(
            np_labels
        ), f"scores labels length ({len(np_scores)}) must be equal to labels length ({len(np_labels)})"

        if self.split_by_label_mode == SplitByLabelMode.NONE:
            far, tpr, _ = metrics.roc_curve(np_labels, np_scores, pos_label=0)
            plt.plot(far, 1 - tpr)
        elif self.split_by_label_mode == SplitByLabelMode.PAS:
            genuine_scores = np_scores[np_labels == 0]
            genuine_labels = np_labels[np_labels == 0]

            attack_scores = np_scores[np_labels != 0]
            attack_labels = np.ones(len(np_labels[np_labels != 0]))

            all_scores = np.concatenate((genuine_scores, attack_scores))
            all_labels = np.concatenate((genuine_labels, attack_labels))

            suffix_label = f" | Attacks {len(attack_scores)}"
            patch = self._plot_curve(
                plt, all_scores, all_labels, suffix_label=suffix_label
            )

            handles = [patch]
            unique_attack_labels = np.unique(np_labels[np_labels != 0])
            for label in unique_attack_labels:
                label_correspondence = self.split_labels_correspondences.get(
                    label, "Unknown"
                )

                attack_filtered_by_label_scores = np_scores[np_labels == label]
                attack_filtered_by_label_labels = np.ones(
                    len(np_labels[np_labels == label])
                )

                partial_scores = np.concatenate(
                    (genuine_scores, attack_filtered_by_label_scores)
                )
                partial_labels = np.concatenate(
                    (genuine_labels, attack_filtered_by_label_labels)
                )

                suffix_label = f" | Attacks {len(attack_filtered_by_label_scores)}"
                patch = self._plot_curve(
                    plt,
                    partial_scores,
                    partial_labels,
                    label_correspondence,
                    suffix_label,
                )

                handles.append(patch)
            plt.legend(handles=handles)
        else:
            genuine_scores = np_scores[np_labels != -1]
            genuine_labels = np.zeros(len(np_labels[np_labels != -1]))

            attack_scores = np_scores[np_labels == -1]
            attack_labels = np.ones(len(np_labels[np_labels == -1]))

            all_scores = np.concatenate((genuine_scores, attack_scores))
            all_labels = np.concatenate((genuine_labels, attack_labels))

            suffix_label = f" | Genuine {len(genuine_scores)}"
            patch = self._plot_curve(
                plt, all_scores, all_labels, suffix_label=suffix_label
            )

            handles = [patch]
            unique_genuine_labels = np.unique(np_labels[np_labels != -1])
            for label in unique_genuine_labels:
                label_correspondence = self.split_labels_correspondences.get(
                    label, "Unknown"
                )

                genuine_filtered_by_label_scores = np_scores[np_labels == label]
                genuine_filtered_by_label_labels = np.zeros(
                    len(np_labels[np_labels == label])
                )

                partial_scores = np.concatenate(
                    (genuine_filtered_by_label_scores, attack_scores)
                )
                partial_labels = np.concatenate(
                    (genuine_filtered_by_label_labels, attack_labels)
                )

                suffix_label = f" | Genuine {len(genuine_filtered_by_label_scores)}"
                patch = self._plot_curve(
                    plt,
                    partial_scores,
                    partial_labels,
                    label_correspondence,
                    suffix_label,
                )

                handles.append(patch)
            plt.legend(handles=handles)
        return plt

    def create_figure(self, scores: Scores):
        np_scores, np_labels, self.split_labels_correspondences = ScoresAndLabelsFormatter.execute(
            scores, self.split_by_label_mode
        )
        plt = self._calculate_det_curve(np_scores, np_labels)
        return plt

    def show(self, scores: Scores):
        plt = self.create_figure(scores)
        plt.show()

    def save(self, output_filename: str, scores: Scores):

        if not os.path.isdir(os.path.dirname(output_filename)):
            raise IOError(
                "Output path [{}] does not exist".format(
                    os.path.dirname(output_filename)
                )
            )

        plt = self.create_figure(scores)
        plt.savefig(output_filename)
        plt.close("all")
