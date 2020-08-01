from typing import Dict

import matplotlib.pyplot as plt

from gradgpad.charts.radar_factory import radar_factory
from gradgpad.tools.create_apcer_detail import ApcerDetail


def create_radar_chart_comparision(
    title: str,
    apcer_by_pai: ApcerDetail,
    output_filename: str,
    correspondences: Dict = None,
    fontsize_vertices=25,
):
    # apcer_by_pai.print()
    values = (title, apcer_by_pai.apcers.values())

    data = [apcer_by_pai.detail_values, values]

    N = len(data[0])
    theta = radar_factory(N, frame="polygon")

    spoke_labels = data.pop(0)
    title, case_data = data[0]

    figsize = (15, 14)
    if N <= 3:
        figsize = (15, 12)

    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(projection="radar"))
    # fig.subplots_adjust(top=0.95, bottom=0.0)

    for d in case_data:
        # line = ax.plot(theta, d)
        ax.fill(theta, d, alpha=0.25)

    ax.set_rgrids(
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        angle=260,
        fontsize=12,
        fontweight="bold",
        color="g",
    )

    ax.set_title(title, ha="center", fontsize=22, fontweight="bold")

    # varlabels = [string.capwords(spoke_label) for spoke_label in spoke_labels]
    varlabels = spoke_labels
    if correspondences:
        varlabels = [
            correspondences[label] if label in correspondences else label
            for label in varlabels
        ]

    ax.set_varlabels(varlabels, fontsize=fontsize_vertices)
    ax.legend(
        apcer_by_pai.apcers.keys(),
        # bbox_to_anchor=(1.05, 1),
        # loc="lower left",
        # ncol=2,
        # mode="expand",
        # borderaxespad=0.0,
        fontsize=18,
    )

    # plt.show()
    plt.tight_layout()
    plt.savefig(output_filename)
