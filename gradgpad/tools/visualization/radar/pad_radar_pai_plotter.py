from typing import Dict, Tuple

from gradgpad.tools.visualization.charts.create_radar_chart_comparison import \
    create_radar_chart_comparison
from gradgpad.tools.visualization.radar.combined_scenario import \
    CombinedScenario
from gradgpad.tools.visualization.radar.create_apcer_detail import (
    WorkingPoint, create_apcer_by_pai)
from gradgpad.tools.visualization.radar.fine_grained_pais_provider import \
    FineGrainedPaisProvider
from gradgpad.tools.visualization.radar.radar_correspondences import (
    BOLD_PAI_CORRESPONDENCES, PAI_REPRESENTATION_ORDER)


class PadRadarPaiPlotter:
    def __init__(
        self,
        title: str,
        working_point: WorkingPoint,
        combined_scenario: CombinedScenario = None,
        representation_order: list = PAI_REPRESENTATION_ORDER,
        correspondences: dict = BOLD_PAI_CORRESPONDENCES,
        fontsize_vertices: int = 20,
        figsize: Tuple = (10, 10),
        format: str = None,
    ):
        self.title = title
        self.working_point = working_point
        self.filter_pais = FineGrainedPaisProvider.by(combined_scenario)
        self.representation_order = representation_order
        self.correspondences = correspondences
        self.fontsize_vertices = fontsize_vertices
        self.figsize = figsize
        self.format = format
        self.apcer_detail = None

    def _calculate_apcer_detail(self, results: dict):
        if self.apcer_detail is None:
            self.apcer_detail = create_apcer_by_pai(
                results, self.working_point, self.filter_pais
            )
            self.apcer_detail.sort_by_detail_values(self.representation_order)

    def create_figure(self, results: Dict[str, dict]):
        self._calculate_apcer_detail(results)
        plt = create_radar_chart_comparison(
            self.title,
            self.apcer_detail,
            self.correspondences,
            fontsize_vertices=self.fontsize_vertices,
            figsize=self.figsize,
        )
        return plt

    def show(self, results: dict):
        plt = self.create_figure(results)
        plt.show()

    def save(self, output_filename: str, results: dict):
        plt = self.create_figure(results)
        plt.tight_layout()
        plt.savefig(output_filename, format=self.format, pad_inches=0)
