from typing import List

from gradgpad.tools.visualization.radar.create_apcer_detail import WorkingPoint

REGULAR_AND_BOLD_PAI_CORRESPONDENCES = {
    "MAKEUP COSMETIC": "Makeup\n" + r"$\bf{Cosmetic}$",
    "MAKEUP IMPERSONATION": "Makeup\n" + r"$\bf{Impersonation}$",
    "MAKEUP OBFUSCATION": "Makeup\n" + r"$\bf{Obfuscation}$",
    "MASK PAPER": "Mask\n" + r"$\bf{Paper}$",
    "MASK RIGID": "Mask\n" + r"$\bf{Rigid}$",
    "MASK SILICONE": "Mask\n" + r"$\bf{Silicone}$",
    "PARTIAL FUNNY EYES": "Partial\n" + r"$\bf{Funny Eyes}$",
    "PARTIAL LOWER HALF": "Partial\n" + r"$\bf{Lower Half}$",
    "PARTIAL UPPER HALF": "Partial\n" + r"$\bf{Upper Half}$",
    "PARTIAL PAPER GLASSES": "Partial\n" + r"$\bf{Paper Glasses}$",
    "PARTIAL PERIOCULAR": "Partial\n" + r"$\bf{Periocular}$",
    "PRINT LOW QUALITY": "Print\n" + r"$\bf{Low Quality}$",
    "PRINT MEDIUM QUALITY": "Print\n" + r"$\bf{Medium Quality}$",
    "PRINT HIGH QUALITY": "Print\n" + r"$\bf{High Quality}$",
    "REPLAY LOW QUALITY": "Replay\n" + r"$\bf{Low Quality}$",
    "REPLAY MEDIUM QUALITY": "Replay\n" + r"$\bf{Medium Quality}$",
    "REPLAY HIGH QUALITY": "Replay\n" + r"$\bf{High Quality}$",
}

PAI_REPRESENTATION_ORDER = [
    "MASK PAPER",
    "MASK RIGID",
    "MASK SILICONE",
    "PRINT LOW QUALITY",
    "PRINT MEDIUM QUALITY",
    "PRINT HIGH QUALITY",
    "REPLAY LOW QUALITY",
    "REPLAY MEDIUM QUALITY",
    "REPLAY HIGH QUALITY",
    "PARTIAL LOWER HALF",
    "PARTIAL PAPER GLASSES",
    "PARTIAL PERIOCULAR",
    "PARTIAL UPPER HALF",
    "MAKEUP COSMETIC",
    "MAKEUP IMPERSONATION",
    "MAKEUP OBFUSCATION",
]

BOLD_PAI_CORRESPONDENCES = {
    "MAKEUP COSMETIC": r"$\bf{Makeup}$" + "\n" + r"$\bf{Cosmetic}$",
    "MAKEUP IMPERSONATION": r"$\bf{Makeup}$" + "\n" + r"$\bf{Impersonation}$",
    "MAKEUP OBFUSCATION": r"$\bf{Makeup}$" + "\n" + r"$\bf{Obfuscation}$",
    "MASK PAPER": r"$\bf{Mask}$" + "\n" + r"$\bf{Paper}$",
    "MASK RIGID": r"$\bf{Mask}$" + "\n" + r"$\bf{Rigid}$",
    "MASK SILICONE": r"$\bf{Mask}$" + "\n" + r"$\bf{Silicone}$",
    "PARTIAL FUNNY EYES": r"$\bf{Partial}$" + "\n" + r"$\bf{Funny Eyes}$",
    "PARTIAL LOWER HALF": r"$\bf{Partial}$" + "\n" + r"$\bf{Lower Half}$",
    "PARTIAL UPPER HALF": r"$\bf{Partial}$" + "\n" + r"$\bf{Upper Half}$",
    "PARTIAL PAPER GLASSES": r"$\bf{Partial}$" + "\n" + r"$\bf{Paper Glasses}$",
    "PARTIAL PERIOCULAR": r"$\bf{Partial}$" + "\n" + r"$\bf{Periocular}$",
    "PRINT LOW QUALITY": r"$\bf{Print}$" + "\n" + r"$\bf{Low Quality}$",
    "PRINT MEDIUM QUALITY": r"$\bf{Print}$" + "\n" + r"$\bf{Medium Quality}$",
    "PRINT HIGH QUALITY": r"$\bf{Print}$" + "\n" + r"$\bf{High Quality}$",
    "REPLAY LOW QUALITY": r"$\bf{Replay}$" + "\n" + r"$\bf{Low Quality}$",
    "REPLAY MEDIUM QUALITY": r"$\bf{Replay}$" + "\n" + r"$\bf{Medium Quality}$",
    "REPLAY HIGH QUALITY": r"$\bf{Replay}$" + "\n" + r"$\bf{High Quality}$",
}


class ConfigRadar:
    def __init__(
        self,
        title: str,
        working_point: WorkingPoint,
        filter_pais: List[str] = None,
        correspondences: dict = None,
        fontsize_vertices: int = 30,
        representation_order: list = PAI_REPRESENTATION_ORDER,
        fancy_correspondences: dict = BOLD_PAI_CORRESPONDENCES,
    ):
        self.title = title
        self.working_point = working_point
        self.filter_pais = filter_pais
        self.correspondences = correspondences
        self.fontsize_vertices = fontsize_vertices
        self.representation_order = representation_order
        self.fancy_correspondences = fancy_correspondences
