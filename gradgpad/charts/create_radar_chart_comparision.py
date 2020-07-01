import matplotlib.pyplot as plt

from gradgpad.charts.radar_factory import radar_factory
from gradgpad.tools.create_apcer_detail import ApcerDetail


def create_radar_chart_comparision(
    title: str, apcer_by_pai: ApcerDetail, output_filename: str
):
    values = (title, apcer_by_pai.apcers.values())

    data = [apcer_by_pai.detail_values, values]

    N = len(data[0])
    theta = radar_factory(N, frame="polygon")

    spoke_labels = data.pop(0)
    title, case_data = data[0]

    fig, ax = plt.subplots(figsize=(15, 16), subplot_kw=dict(projection="radar"))
    fig.subplots_adjust(top=0.95, bottom=0.05)

    ax.set_rgrids(
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        angle=260,
        fontsize=12,
        fontweight="bold",
        color="g",
    )

    ax.set_title(
        title, position=(0.5, 1.11), ha="center", fontsize=22, fontweight="bold"
    )
    for d in case_data:
        # line = ax.plot(theta, d)
        ax.fill(theta, d, alpha=0.25)

    # varlabels = [string.capwords(spoke_label) for spoke_label in spoke_labels]
    varlabels = spoke_labels
    ax.set_varlabels(varlabels, fontsize=15)
    ax.legend(
        apcer_by_pai.apcers.keys(),
        bbox_to_anchor=(0.0, 1.04, 1.0, 0.102),
        loc="lower left",
        ncol=2,
        mode="expand",
        borderaxespad=0.0,
        fontsize=18,
    )

    # plt.show()
    plt.savefig(output_filename)
