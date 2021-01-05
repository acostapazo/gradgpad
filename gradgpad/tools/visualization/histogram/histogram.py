import copy
import os

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import warnings

from gradgpad.foundations.scores import Scores
from gradgpad.tools.visualization.histogram.split_by_level_mode import SplitByLabelMode

warnings.filterwarnings("ignore", module="matplotlib")


def valid_labels(np_labels):
    if np.any(np_labels == None):  # noqa
        return False
    else:
        return True


class Histogram:
    def __init__(
        self,
        title="Histogram",
        plot_vertical_line_on_value=None,
        legend_vertical_line="",
        normalize=False,
        y_max_value=None,
        split_by_label_mode: SplitByLabelMode = SplitByLabelMode.NONE,
        genuine_label=0,
    ):
        """
        This function saves a static histogram

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
        """
        self.title = title
        self.plot_vertical_line_on_value = plot_vertical_line_on_value
        self.legend_vertical_line = legend_vertical_line
        self.normalize = normalize
        self.y_max_value = y_max_value
        self.split_by_label_mode = split_by_label_mode
        self.split_labels_correspondences = None
        self.genuine_label = genuine_label

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
        colors = {
            -1: "red",
            0: "green",
            1: "blue",
            2: "orange",
            3: "magenta",
            4: "indigo",
            5: "yellowgreen",
            6: "hotpink",
            7: "springgreen",
        }

        legend = []
        max_value = 0
        for label in np.unique(np_labels):
            scores_subdivision = np_scores[np_labels == label]
            hist_subdivision, edges_subdivision = np.histogram(
                scores_subdivision, bins=50
            )
            if self.normalize:
                hist_subdivision = (
                    hist_subdivision / hist_subdivision.max()
                )  # TODO REVIEW

            plt.bar(
                (edges_subdivision[1:] + edges_subdivision[:-1]) * 0.5,
                hist_subdivision,
                width=(edges_subdivision[1] - edges_subdivision[0]),
                facecolor=colors[label],
                alpha=0.5,
            )

            label_correspondence = self.split_labels_correspondences.get(label)

            impostor_subtype_patch = mpatches.Patch(
                color=colors[label],
                label=f"{label_correspondence} ({len(scores_subdivision)})",
            )
            legend.append(impostor_subtype_patch)

            if max(hist_subdivision) > max_value:
                max_value = max(hist_subdivision)

        # genuine = np_scores[np_labels == self.genuine_label]
        # hist_gen, edges_gen = np.histogram(genuine, bins=50)
        # if self.normalize:
        #     hist_gen = hist_gen / hist_gen.max()
        #
        # impostors = np_scores[np_labels != self.genuine_label]
        #
        # hist_impos, edges_impos = np.histogram(impostors, bins=50)
        # if self.normalize:
        #     hist_impos = hist_impos / hist_impos.max()
        #
        # red_patch = mpatches.Patch(
        #     color="red", label="Impostors ({})".format(len(impostors)), alpha=0.5
        # )
        # green_patch = mpatches.Patch(
        #     color="green", label="Genuine ({})".format(len(genuine)), alpha=0.5
        # )

        # for label in range(1, max(np_labels) + 1):
        #     impostors_subtype = np_scores[np_labels == label]
        #     hist_impos_subtype, edges_impos_subtype = np.histogram(
        #         impostors_subtype, bins=50
        #     )
        #     if self.normalize:
        #         hist_impos_subtype = hist_impos_subtype / hist_impos_subtype.max()
        #
        #     plt.bar(
        #         (edges_impos[1:] + edges_impos[:-1]) * 0.5,
        #         hist_impos_subtype,
        #         width=(edges_impos_subtype[1] - edges_impos_subtype[0]),
        #         facecolor=colors[label],
        #         alpha=0.5,
        #     )
        #
        #     label_correspondence = self.split_labels_correspondences.get(label)
        #
        #     impostor_subtype_patch = mpatches.Patch(
        #         color=colors[label],
        #         label=f"Impostors {label_correspondence} ({len(impostors_subtype)})",
        #     )
        #     legend.append(impostor_subtype_patch)
        return legend, max_value

    def _calculate_histogram(self, np_scores, np_labels):

        scores = copy.deepcopy(np.ravel(np_scores))

        plt.figure()
        plt.xlabel("Score")
        plt.ylabel("Count")
        plt.title(self.title)

        if valid_labels(np_labels):
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

    def _get_operative_data(self, scores):
        np_scores = scores.get_numpy_scores()

        if self.split_by_label_mode == SplitByLabelMode.NONE:
            np_labels = scores.get_numpy_labels()
        elif self.split_by_label_mode == SplitByLabelMode.PAS:
            np_labels = scores.get_numpy_labels_by_scenario()
            self.split_labels_correspondences = {
                0: "Genuine",
                1: "PAS Type I",
                2: "PAS Type II",
                3: "PAS Type III",
            }
        elif self.split_by_label_mode == SplitByLabelMode.SEX:
            np_labels = scores.get_numpy_labels_by_sex()
            self.split_labels_correspondences = {-1: "IMPOSTOR", 0: "MALE", 1: "FEMALE"}
        elif self.split_by_label_mode == SplitByLabelMode.AGE:
            np_labels = scores.get_numpy_labels_by_age()
            self.split_labels_correspondences = {
                -1: "IMPOSTOR",
                0: "YOUNG",
                1: "ADULT",
                2: "SENIOR",
            }
        elif self.split_by_label_mode == SplitByLabelMode.SKIN_TONE:
            np_labels = scores.get_numpy_labels_by_skin_tone()
            self.split_labels_correspondences = {
                -1: "IMPOSTOR",
                0: "YOUNG",
                1: "ADULT",
                3: "SENIOR",
            }

        return np_scores, np_labels

    def show(self, scores: Scores):
        np_scores, np_labels = self._get_operative_data(scores)
        plt = self._calculate_histogram(np_scores, np_labels)
        plt.show()

    def save(self, output_filename: str, scores: Scores):

        if not os.path.isdir(os.path.dirname(output_filename)):
            raise IOError(
                "Output path [{}] does not exist".format(
                    os.path.dirname(output_filename)
                )
            )

        np_scores, np_labels = self._get_operative_data(scores)
        plt = self._calculate_histogram(np_scores, np_labels)
        plt.savefig(output_filename)
        plt.close("all")
