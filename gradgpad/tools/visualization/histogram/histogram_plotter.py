import copy
import os

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import warnings

from typing import List, Tuple
from gradgpad.foundations.scores import Scores
from gradgpad.tools.visualization.colors import COLORS_LABEL_CORRESPONDENCES
from gradgpad.tools.visualization.histogram.split_by_level_mode import SplitByLabelMode
from gradgpad.tools.visualization.interface_plotter import IPlotter
from gradgpad.tools.visualization.scores_and_labels_formatter import (
    ScoresAndLabelsFormatter,
)

warnings.filterwarnings("ignore", module="matplotlib")


class HistogramPlotter(IPlotter):
    def __init__(
        self,
        title="Histogram",
        plot_vertical_line_on_value=None,
        legend_vertical_line="",
        normalize=False,
        y_max_value=None,
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
        plot_vertical_line_on_value: float
            value to plot a vertical line in a specific value
        legend_vertical_line: str
            Legend of plotted vertical line
        normalize: boolean
            Determines whether it normalizes the hist (Default False)
        y_max_value: float
            Limit the max value of the y axis
        split_by_label_mode: SplitByLabelMode
            Select the way of subdivision of labels
        genuine_label: int
            label that corresponds to the genuine class
        exclude_labels: list
            List of excluded labels
        figsize: Tuple
            size of the figure
        """
        self.title = title
        self.plot_vertical_line_on_value = plot_vertical_line_on_value
        self.legend_vertical_line = legend_vertical_line
        self.normalize = normalize
        self.y_max_value = y_max_value
        self.split_by_label_mode = split_by_label_mode
        self.split_labels_correspondences = None
        self.genuine_label = genuine_label
        self.exclude_labels = exclude_labels
        self.figsize = figsize

    def _calculate_genuine_and_impostor_histogram(self, np_scores, np_labels, plt):
        # Genuine
        genuine = np_scores[np_labels == self.genuine_label]
        hist_gen, edges_gen = np.histogram(genuine, bins=50)
        if self.normalize:
            hist_gen = hist_gen / hist_gen.max()
        plt.bar(
            (edges_gen[1:] + edges_gen[:-1]) * 0.5,
            hist_gen,
            width=(edges_gen[1] - edges_gen[0]),
            facecolor="g",
            alpha=0.5,
        )
        # Impostor
        impostors = np_scores[np_labels != self.genuine_label]
        hist_impos, edges_impos = np.histogram(impostors, bins=50)
        if self.normalize:
            hist_impos = hist_impos / hist_impos.max()
        plt.bar(
            (edges_impos[1:] + edges_impos[:-1]) * 0.5,
            hist_impos,
            width=(edges_impos[1] - edges_impos[0]),
            facecolor="r",
            alpha=0.5,
        )

        red_patch = mpatches.Patch(
            color="red", label="Impostors ({})".format(len(impostors)), alpha=0.5
        )
        green_patch = mpatches.Patch(
            color="green", label="Genuine ({})".format(len(genuine)), alpha=0.5
        )

        legend = [green_patch, red_patch]
        max_value = max(hist_gen.max(), hist_impos.max())
        return legend, max_value

    def _calculate_subdivided_histogram(self, np_scores, np_labels, plt):

        unique_labels = np.unique(np_labels)

        legend = []
        max_value = 0
        alpha = 0.9
        alpha_interval_decreasing = 0.5 / len(unique_labels)
        for label in unique_labels:
            color = COLORS_LABEL_CORRESPONDENCES.get(label)

            if self.exclude_labels and label in self.exclude_labels:
                continue
            scores_subdivision = np_scores[np_labels == label]
            hist_subdivision, edges_subdivision = np.histogram(
                scores_subdivision, bins=50
            )
            if self.normalize:
                hist_subdivision = hist_subdivision / hist_subdivision.max()

            if alpha >= 0.5:
                alpha -= alpha_interval_decreasing

            plt.bar(
                (edges_subdivision[1:] + edges_subdivision[:-1]) * 0.5,
                hist_subdivision,
                width=(edges_subdivision[1] - edges_subdivision[0]),
                facecolor=color,
                alpha=alpha,
            )

            label_correspondence = self.split_labels_correspondences.get(
                label, "Unknown"
            )

            patch = mpatches.Patch(
                color=color, label=f"{label_correspondence} ({len(scores_subdivision)})"
            )
            legend.append(patch)

            if max(hist_subdivision) > max_value:
                max_value = max(hist_subdivision)

        return legend, max_value

    def _calculate_histogram(self, np_scores, np_labels):

        scores = copy.deepcopy(np.ravel(np_scores))

        plt.close()
        plt.figure(figsize=(10, 10))
        plt.xlabel("Score")
        plt.ylabel("Count")
        plt.title(self.title)

        if self.valid_labels(np_labels):
            labels = copy.deepcopy(np.ravel(np_labels))
            assert len(scores) == len(
                labels
            ), f"scores labels length ({len(scores)}) must be equal to labels length ({len(labels)})"

            if self.split_by_label_mode == SplitByLabelMode.NONE:
                legend, max_value = self._calculate_genuine_and_impostor_histogram(
                    np_scores, np_labels, plt
                )
            else:
                legend, max_value = self._calculate_subdivided_histogram(
                    np_scores, np_labels, plt
                )

            if self.y_max_value:
                axes = plt.gca()
                axes.set_ylim([0, self.y_max_value])

            if self.plot_vertical_line_on_value is not None:
                x, y = (
                    [
                        self.plot_vertical_line_on_value,
                        self.plot_vertical_line_on_value,
                    ],
                    [0, max_value],
                )
                th_line, = plt.plot(x, y, "b--", label=self.legend_vertical_line)
                legend = legend + [th_line]

            plt.legend(handles=legend)

        else:
            hist, edges = np.histogram(scores, bins=50)

            if self.normalize:
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

            if self.plot_vertical_line_on_value is not None:
                x, y = (
                    [
                        self.plot_vertical_line_on_value,
                        self.plot_vertical_line_on_value,
                    ],
                    [0, max_value],
                )
                th_line, = plt.plot(x, y, "b--", label=self.legend_vertical_line)
                plt.legend(handles=[patch, th_line])
            else:
                plt.legend(handles=[patch])

        return plt

    def create_figure(self, scores: Scores):
        np_scores, np_labels, self.split_labels_correspondences = ScoresAndLabelsFormatter.execute(
            scores, self.split_by_label_mode, self.exclude_labels
        )

        plt = self._calculate_histogram(np_scores, np_labels)
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
