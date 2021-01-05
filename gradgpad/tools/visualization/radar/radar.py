from gradgpad.tools.visualization.radar.create_apcer_detail import create_apcer_by_pai
from gradgpad.tools.evaluation.charts.create_radar_chart_comparison import (
    create_radar_chart_comparison,
)
from gradgpad.tools.visualization.radar.config_radar import ConfigRadar


class Radar:
    def __init__(self, config_radar: ConfigRadar):
        self.config_radar = config_radar
        self.apcer_detail = None

    def _calculate_apcer_detail(self, results: dict):
        if self.apcer_detail is None:
            self.apcer_detail = create_apcer_by_pai(
                results, self.config_radar.working_point, self.config_radar.filter_pais
            )
            self.apcer_detail.sort_by_detail_values(
                self.config_radar.representation_order
            )

    def save(self, output_filename: str, results: dict):
        self._calculate_apcer_detail(results)
        create_radar_chart_comparison(
            self.config_radar.title,
            self.apcer_detail,
            output_filename,
            self.config_radar.fancy_correspondences,
            20,
        )

    def show(self, results: dict):
        self._calculate_apcer_detail(results)
        create_radar_chart_comparison(
            self.config_radar.title,
            self.apcer_detail,
            None,
            self.config_radar.fancy_correspondences,
            20,
        )
