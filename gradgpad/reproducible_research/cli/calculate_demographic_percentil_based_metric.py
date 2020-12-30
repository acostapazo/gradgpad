import os

import numpy as np
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt

from gradgpad.foundations.metrics.metrics import Metrics
from gradgpad.reproducible_research.cli.calculate_demographic_bias_metric import (
    calculate_demographic_bias_metric,
)
from gradgpad.foundations.scores.approach import Approach
from gradgpad.foundations.scores.protocol import Protocol
from gradgpad.foundations.scores.scores_provider import ScoresProvider
from gradgpad.foundations.scores.subset import Subset

COLORS = {
    "MALE": "b",
    "FEMALE": "g",
    "YOUNG": "g",
    "ADULT": "b",
    "SENIOR": "y",
    "ATTACKS": "r",
    "YELLOW": "y",
    "PINK": "pink",
    "BROWN": "brown",
}

MARKERS = {"ATTACKS": "v"}


def calculate_demographic_percentile_based_metric(
    output_path: str, protocol: Protocol = Protocol.GRANDTEST
):
    print("> Demographic | Calculating Percentile Graphs...")

    output_path_percentiles = (
        f"{output_path}/demographic/percentiles_with_metric/{protocol.value}"
    )
    os.makedirs(output_path_percentiles, exist_ok=True)

    quality_scores_devel = ScoresProvider.get(
        approach=Approach.QUALITY_RBF, protocol=protocol, subset=Subset.DEVEL
    )
    quality_scores_test = ScoresProvider.get(
        approach=Approach.QUALITY_RBF, protocol=protocol, subset=Subset.TEST
    )
    quality_metrics = Metrics(
        devel_scores=quality_scores_devel, test_scores=quality_scores_test
    )
    auxiliary_scores_devel = ScoresProvider.get(
        approach=Approach.AUXILIARY, protocol=protocol, subset=Subset.DEVEL
    )
    auxiliary_scores_test = ScoresProvider.get(
        approach=Approach.AUXILIARY, protocol=protocol, subset=Subset.TEST
    )
    auxiliary_metrics = Metrics(
        devel_scores=auxiliary_scores_devel, test_scores=auxiliary_scores_test
    )

    # balanced
    # quality_balanced_scores_devel = ScoresProvider.get(
    #    approach=Approach.QUALITY_RBF_BALANCED, protocol=protocol, subset=Subset.DEVEL
    # )
    # quality_balanced_scores_test = ScoresProvider.get(
    #    approach=Approach.QUALITY_RBF_BALANCED, protocol=protocol, subset=Subset.TEST
    # )
    # quality_balanced_metrics = Metrics(
    #    devel_scores=quality_balanced_scores_devel,
    #    test_scores=quality_balanced_scores_test,
    # )

    approaches = {
        "Quality": (
            quality_scores_test,
            quality_metrics.get_frr_th(Subset.TEST, 0.05),
            quality_metrics.get_frr_th(Subset.TEST, 0.15),
        ),
        "Auxiliary": (
            auxiliary_scores_test,
            auxiliary_metrics.get_frr_th(Subset.TEST, 0.05),
            auxiliary_metrics.get_frr_th(Subset.TEST, 0.15),
        ),
    }

    p = np.linspace(0, 100, 6001)
    interpolation = "linear"

    demographic_percentiles = {}
    for (
        approach,
        (scores, lower_frr_th_devel, higher_frr_th_test),
    ) in approaches.items():

        demographic_scores = {
            "sex": scores.get_fair_sex_subset(),
            "age": scores.get_fair_age_subset(),
            # "skin_tone": scores.get_fair_skin_tone_subset(),
            "grouped_skin_tone": scores.get_fair_grouped_skin_tone_subset(),
            "attacks": {"attacks": scores.get_attacks_with_ids()},
        }

        for demographic, fair_scores in demographic_scores.items():
            if demographic == "attacks":
                continue

            percentiles = {}

            for sub_demographic, scores_demographic in fair_scores.items():

                values = np.array(list(scores_demographic.values()))

                percentiles[sub_demographic] = np.percentile(
                    values, p, interpolation=interpolation
                )

            attack_values = np.array(list(scores.get_attacks_with_ids().values()))
            percentiles["ATTACKS"] = np.percentile(
                attack_values, p, interpolation=interpolation
            )

            if demographic not in demographic_percentiles:
                demographic_percentiles[demographic] = {
                    approach: (percentiles, lower_frr_th_devel, higher_frr_th_test)
                }
            else:
                demographic_percentiles[demographic][approach] = (
                    percentiles,
                    lower_frr_th_devel,
                    higher_frr_th_test,
                )

    calculate_demographic_bias_metric(
        demographic_percentiles, approaches.keys(), output_path_percentiles
    )

    for demographic, approaches_percentiles in demographic_percentiles.items():
        fig, axlist = plt.subplots(1, 2)  # sharex=True, sharey=True
        subplot_index = 0
        for (
            approach,
            (percentiles, lower_frr_th_devel, higher_frr_th_test),
        ) in approaches_percentiles.items():
            for sub_demographic, percentil in percentiles.items():
                values = p
                if sub_demographic != "ATTACKS":
                    values = 100 - p

                axlist[subplot_index].plot(
                    percentil,
                    values,
                    label=sub_demographic.title().replace("_", " "),
                    linestyle="-",
                    color=COLORS.get(sub_demographic),
                    marker=MARKERS.get(sub_demographic),
                    markevery=300,
                )
                axlist[subplot_index].yaxis.set_major_formatter(
                    mtick.PercentFormatter()
                )
                # x, y = [0, 100], [lower_frr_th_devel, lower_frr_th_devel]
                # axlist[subplot_index].plot(y, x, "b--", label="FRR 5 %", color="gray")
                # x, y = [0, 100], [higher_frr_th_test, higher_frr_th_test]
                # axlist[subplot_index].plot(y, x, "b--", label="FRR 15 %", color="gray")
                axlist[subplot_index].fill_between(
                    [lower_frr_th_devel, higher_frr_th_test],
                    100,
                    facecolor="gray",
                    alpha=0.2,
                    label="Working Points",
                )

                axlist[subplot_index].set_title(approach)

                axlist[subplot_index].grid(
                    b=True, which="major", color="#CCCCCC", linestyle="--"
                )
                axlist[subplot_index].grid(
                    b=True, which="minor", color="#CCCCCC", linestyle=":"
                )

                # axlist[subplot_index].xaxis.set_ticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
                axlist[subplot_index].yaxis.set_ticks(
                    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                )

                if subplot_index == 1:
                    axlist[subplot_index].yaxis.tick_right()

                # axlist[subplot_index].xticks(rotation=30)
                for tick in axlist[subplot_index].get_yticklabels():
                    tick.set_rotation(55)
                for tick in axlist[subplot_index].get_xticklabels():
                    tick.set_rotation(45)

            subplot_index += 1

        # fig.text(0.5, 0.04, "Percentil", ha="center")
        # fig.text(0.02, 0.59, "Score", va="center", rotation="vertical")

        # fig.text(0.5, 0.04, "Score", ha="center")
        fig.text(0.01, 0.59, "BPCER", va="center", rotation="vertical")
        fig.text(0.97, 0.59, "APCER", va="center", rotation="vertical", color="red")

        fig.subplots_adjust(
            top=0.9, left=0.1, right=0.9, bottom=0.15
        )  # create some space below the plots by increasing the bottom-value

        legend_without_duplicate_labels(axlist.flatten()[-2])

        filename = f"{output_path_percentiles}/percentile_comparison_{demographic}.png"

        # plt.tight_layout()
        plt.savefig(filename)
        plt.tight_layout()
        plt.close("all")


def legend_without_duplicate_labels(ax):
    handles, labels = ax.get_legend_handles_labels()
    unique = [
        (h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]
    ]
    unique_values = [
        (h, l) for h, l in sorted(unique, key=lambda tup: tup[1]) if "EER" not in l
    ]
    unique_values_eer = [(h, l) for h, l in unique if "EER" in l]
    unique_sorted = unique_values + unique_values_eer

    ncol = len(unique_sorted)
    last_values = [
        (line, label)
        for line, label in unique_sorted
        if label == "Attacks" or label == "Working Points"
    ]
    first_values = [
        (line, label)
        for line, label in unique_sorted
        if label != "Attacks" and label != "Working Points"
    ]
    unique_sorted = first_values + last_values

    ax.legend(
        *zip(*unique_sorted), loc="upper center", bbox_to_anchor=(1.1, -0.10), ncol=ncol
    )
