from typing import List, Tuple

from gradgpad.tools.visualization.radar.create_apcer_detail import (
    create_apcer_by_pai,
    WorkingPoint,
)
from gradgpad.tools.visualization.charts.create_radar_chart_comparison import (
    create_radar_chart_comparison,
)
from gradgpad.tools.visualization.radar.radar_correspondences import (
    PAI_REPRESENTATION_ORDER,
    BOLD_PAI_CORRESPONDENCES,
)


class Radar:
    def __init__(
        self,
        title: str,
        working_point: WorkingPoint,
        filter_pais: List[str] = None,
        correspondences: dict = None,
        fontsize_vertices: int = 30,
        representation_order: list = PAI_REPRESENTATION_ORDER,
        fancy_correspondences: dict = BOLD_PAI_CORRESPONDENCES,
        figsize: Tuple = (10, 10),
    ):
        self.title = title
        self.working_point = working_point
        self.filter_pais = filter_pais
        self.correspondences = correspondences
        self.fontsize_vertices = fontsize_vertices
        self.representation_order = representation_order
        self.fancy_correspondences = fancy_correspondences
        self.apcer_detail = None
        self.figsize = figsize

    def _calculate_apcer_detail(self, results: dict):
        if self.apcer_detail is None:
            self.apcer_detail = create_apcer_by_pai(
                results, self.working_point, self.filter_pais
            )
            self.apcer_detail.sort_by_detail_values(self.representation_order)

    def save(self, output_filename: str, results: dict):
        self._calculate_apcer_detail(results)
        create_radar_chart_comparison(
            self.title,
            self.apcer_detail,
            output_filename,
            self.fancy_correspondences,
            20,
            figsize=self.figsize,
        )

    def show(self, results: dict):
        self._calculate_apcer_detail(results)
        create_radar_chart_comparison(
            self.title,
            self.apcer_detail,
            None,
            self.fancy_correspondences,
            20,
            figsize=self.figsize,
        )
