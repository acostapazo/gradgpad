from typing import Tuple

from gradgpad import Demographic
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

from gradgpad.foundations.scores import Scores
from gradgpad.tools.visualization.interface_plotter import IPlotter
from gradgpad.tools.visualization.percentile.legend_tools import (
    legend_without_duplicate_labels,
    COLORS,
    MARKERS,
)


class BiasPercentilePlotter(IPlotter):
    def __init__(
        self,
        title: str,
        demographic: Demographic,
        working_point: Tuple[float, float] = None,
        figsize: Tuple[float, float] = (10, 10),
    ):
        """
        Parameters
        ----------
        title: str
            Title of the figure
        demographic: Demographic
            Select the demographic subgroup
        working_point: int
            label that corresponds to the genuine class
        figsize: Tuple
            size of the figure
        """
        self.title = title
        self.demographic = demographic
        self.p = np.linspace(0, 100, 6001)
        self.interpolation = "linear"
        self.working_point = working_point
        self.figsize = figsize

    def _calculate_percentiles(self, scores):
        percentiles = {}

        if self.demographic == Demographic.SEX:
            fair_scores = scores.get_fair_sex_subset()
        elif self.demographic == Demographic.AGE:
            fair_scores = scores.get_fair_age_subset()
        elif self.demographic == Demographic.SKIN_TONE:
            fair_scores = scores.get_fair_skin_tone_subset()
        elif self.demographic == Demographic.GROUPED_SKIN_TONE:
            fair_scores = scores.get_fair_grouped_skin_tone_subset()
        else:
            fair_scores = {}

        fair_scores["ATTACKS"] = scores.get_attacks_with_ids()

        for sub_demographic, scores_demographic in fair_scores.items():
            values = np.array(list(scores_demographic.values()))
            percentiles[sub_demographic] = np.percentile(
                values, self.p, interpolation=self.interpolation
            )
        return percentiles

    def create_figure(self, scores: Scores):
        percentiles = self._calculate_percentiles(scores)

        plt.close()
        fig, ax = plt.subplots(figsize=self.figsize)

        ax.set_title(self.title)
        ax.set_ylabel("BPCER")
        ax.set_ylim(0, 105)
        ax.text(
            1.03,
            0.51,
            "APCER",
            va="center",
            rotation="vertical",
            color="red",
            transform=ax.transAxes,
        )

        for sub_demographic, percentile in percentiles.items():

            values = self.p
            if sub_demographic != "ATTACKS":
                values = 100 - self.p

            ax.plot(
                percentile,
                values,
                label=sub_demographic.title().replace("_", " "),
                linestyle="-",
                color=COLORS.get(sub_demographic),
                marker=MARKERS.get(sub_demographic),
                markevery=300,
            )

        ax.yaxis.set_major_formatter(mtick.PercentFormatter())

        if self.working_point:
            ax.fill_between(
                self.working_point,
                100,
                facecolor="gray",
                alpha=0.2,
                label="Working Points",
            )

        ax.grid(b=True, which="major", color="#CCCCCC", linestyle="--")
        ax.grid(b=True, which="minor", color="#CCCCCC", linestyle=":")

        ax.yaxis.set_ticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

        for tick in ax.get_yticklabels():
            tick.set_rotation(55)
        for tick in ax.get_xticklabels():
            tick.set_rotation(45)

        legend_without_duplicate_labels(ax)
        return plt

    def show(self, scores):
        plt = self.create_figure(scores)
        plt.show()
        plt.tight_layout()
        plt.close("all")

    def save(self, output_filename: str, scores: Scores):
        plt = self.create_figure(scores)
        plt.savefig(output_filename)
        plt.close("all")
