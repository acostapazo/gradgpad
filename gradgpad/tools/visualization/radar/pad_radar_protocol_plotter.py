from typing import Tuple, Dict

from gradgpad.foundations.scores.protocol import Protocol
from gradgpad.foundations.annotations.grained_pai_mode import GrainedPaiMode
from gradgpad.tools.visualization.radar.create_apcer_detail import (
    WorkingPoint,
    create_apcer_by_subprotocol,
)
from gradgpad.tools.visualization.charts.create_radar_chart_comparison import (
    create_radar_chart_comparison,
)

DATASET_CORRESPONDENCES = {
    "casia-fasd": "CASIA-FASD",
    "uvad": "UVAD",
    "threedmad": "3DMAD",
    "siw-m": "SiW-M",
    "siw": "SiW",
    "rose-youtu": "Rose-Youtu",
    "replay-mobile": "Replay-Mobile",
    "replay-attack": "Replay-Attack",
    "oulu-npu": "Oulu-NPU",
    "msu-mfsd": "MSU-MFSD",
    "hkbuV2": "$HKBU_{V2}$",
    "hkbu": "$HKBU_{v1}$",
    "csmad": "CSMAD",
}
CROSS_DEVICE_CORRESPONDENCES = {
    "digital_camera": "Digital Camera",
    "mobile_tablet": "Mobile | Tablet",
    "webcam": "Webcam",
}

UNSEEN_ATTACK_CORRESPONDENCES = {
    "mask": "Mask",
    "makeup": "Makeup",
    "partial": "Partial",
    "replay": "Replay",
    "print": "Print",
}
CORRESPONDENCES = {
    "lodo": DATASET_CORRESPONDENCES,
    "cross_dataset": DATASET_CORRESPONDENCES,
    "intradataset": DATASET_CORRESPONDENCES,
    "cross_device": CROSS_DEVICE_CORRESPONDENCES,
    "unseen_attack": UNSEEN_ATTACK_CORRESPONDENCES,
}


class PadRadarProtocolPlotter:
    def __init__(
        self,
        title: str,
        working_point: WorkingPoint,
        grained_pai_mode: GrainedPaiMode,
        protocol: Protocol = None,
        correspondences: dict = None,
        fontsize_vertices: int = 30,
        figsize: Tuple = (10, 10),
    ):
        self.title = title
        self.working_point = working_point
        self.grained_pai_mode = grained_pai_mode
        self.protocol = protocol
        self.correspondences = correspondences
        self.fontsize_vertices = fontsize_vertices
        self.fancy_correspondences = CORRESPONDENCES.get(self.protocol.value)
        self.apcer_detail = None
        self.figsize = figsize

    def _calculate_apcer_detail(self, results: dict):
        if self.apcer_detail is None:
            self.apcer_detail = create_apcer_by_subprotocol(
                results,
                self.working_point,
                f"{self.protocol.value}_",
                self.grained_pai_mode,
            )

    def create_figure(self, results: Dict[str, dict]):
        self._calculate_apcer_detail(results)
        plt = create_radar_chart_comparison(
            self.title,
            self.apcer_detail,
            self.fancy_correspondences,
            17,
            figsize=self.figsize,
        )
        return plt

    def show(self, results: dict):
        plt = self.create_figure(results)
        plt.show()

    def save(self, output_filename: str, results: dict):
        plt = self.create_figure(results)
        plt.tight_layout()
        plt.savefig(output_filename)
