import os

from PIL import Image

from gradgpad.foundations.results.results_provider import ResultsProvider
from gradgpad.foundations.scores.approach import Approach
from gradgpad.foundations.scores.protocol import Protocol
from gradgpad.tools.visualization.radar.create_apcer_detail import (
    WorkingPoint,
    create_apcer_by_pai,
)
from gradgpad.tools.visualization.charts.create_radar_chart_comparison import (
    create_radar_chart_comparison,
)

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


def calculate_lifelong_learning_apcer_generalization_protocols(output_path: str):
    print("> Lifelong Learning | Calculating PAD-radar (APCER by PAI)...")

    output_path_apcer_by_pais = f"{output_path}/radar/lifelong_learning_apcer_by_pais"
    os.makedirs(output_path_apcer_by_pais, exist_ok=True)

    # results_with_two_qualities = {
    #     "Quality SVM RBF": ResultsProvider.get(
    #         Approach.QUALITY_RBF, protocol=Protocol.GRANDTEST
    #     ),
    #      "Quality SVM LINEAR": ResultsProvider.get(
    #          Approach.QUALITY_LINEAR, protocol=Protocol.GRANDTEST
    #      ),
    #     "Auxiliary": ResultsProvider.get(
    #         Approach.AUXILIARY, protocol=Protocol.GRANDTEST
    #     ),
    # }

    results = {
        "Auxiliary (Only Type I)": ResultsProvider.get(
            Approach.AUXILIARY, protocol=Protocol.GRANDTEST
        ),
        "Auxiliary": ResultsProvider.get(
            Approach.AUXILIARY, protocol=Protocol.GRANDTEST_TYPE_I_AND_II
        ),
        "CL Auxiliary": ResultsProvider.get(
            Approach.CONTINUAL_LEARNING_AUXILIARY,
            protocol=Protocol.GRANDTEST_TYPE_I_AND_II,
        ),
    }

    selected_working_points = {
        "APCER @ BPCER 1 %": WorkingPoint.BPCER_1,
        "APCER @ BPCER 5 %": WorkingPoint.BPCER_5,
        "APCER @ BPCER 10 %": WorkingPoint.BPCER_10,
        "APCER @ BPCER 15 %": WorkingPoint.BPCER_15,
        "APCER @ BPCER 20 %": WorkingPoint.BPCER_20,
        "APCER @ BPCER 25 %": WorkingPoint.BPCER_25,
        "APCER @ BPCER 30 %": WorkingPoint.BPCER_30,
        "APCER @ BPCER 35 %": WorkingPoint.BPCER_35,
        "APCER @ BPCER 40 %": WorkingPoint.BPCER_40,
        "APCER @ BPCER 45 %": WorkingPoint.BPCER_45,
        "APCER @ BPCER 50 %": WorkingPoint.BPCER_50,
    }

    filenames_pais_types = {}

    for title, working_point in selected_working_points.items():
        pais_group = {
            "test_all": [
                "print_low_quality",
                "print_medium_quality",
                "print_high_quality",
                "replay_low_quality",
                "replay_medium_quality",
                "replay_high_quality",
                "mask_paper",
                "mask_rigid",
                "mask_silicone",
                "makeup_impersonation",
                "partial_lower_half",
                "partial_periocular",
                "partial_upper_half",
                "makeup_cosmetic",
                "makeup_obfuscation",
                "partial_funny_eyes",
                "partial_paper_glasses",
            ],
            "test_type_I_and_II": [
                "print_low_quality",
                "print_medium_quality",
                "print_high_quality",
                "replay_low_quality",
                "replay_medium_quality",
                "replay_high_quality",
                "mask_paper",
                "mask_rigid",
                "mask_silicone",
                "makeup_impersonation",
                "partial_lower_half",
                "partial_periocular",
                "partial_upper_half",
            ],
        }

        for pais_type, filter_pais in pais_group.items():
            filename = f"{output_path_apcer_by_pais}/grandtest_trained_type_pai_I_and_II_{pais_type}_{working_point.value}_radar_chart.png"

            if pais_type not in filenames_pais_types:
                filenames_pais_types[pais_type] = [filename]
            else:
                filenames_pais_types[pais_type].append(filename)

            apcer_detail = create_apcer_by_pai(results, working_point, filter_pais)

            apcer_detail.sort_by_detail_values(PAI_REPRESENTATION_ORDER)
            create_radar_chart_comparison(
                title, apcer_detail, filename, BOLD_PAI_CORRESPONDENCES, 20
            )

    if filenames_pais_types:
        output_path_apcer_by_pais_gifs = f"{output_path_apcer_by_pais}/gifs/"
        os.makedirs(output_path_apcer_by_pais_gifs, exist_ok=True)

        for pais_type, filenames in filenames_pais_types.items():
            img, *imgs = [Image.open(f) for f in filenames]
            filename_gif = f"{output_path_apcer_by_pais_gifs}/grandtest_trained_type_pai_I_and_II_{pais_type}.gif"
            img.save(
                fp=filename_gif,
                format="GIF",
                append_images=imgs,
                save_all=True,
                duration=1500,
            )
