from gradgpad.charts.create_radar_chart_comparision import (
    create_radar_chart_comparision,
)
from gradgpad.reproducible_research.results.results_provider import ResultsProvider
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.tools.create_apcer_detail import WorkingPoint, create_apcer_by_pai


def calculate_apcer_by_pai(output_path: str):
    print("Calculating APCER by PAI...")

    # approaches = {
    #     "Quality SVM RBF": {
    #         subset.name: ScoresProvider.get(
    #             approach=Approach.QUALITY_RBF,
    #             protocol=Protocol.GRANDTEST,
    #             subset=subset,
    #         )
    #         for subset in Subset.options()
    #     },
    #     "Quality SVM Linear": {
    #         subset.name: ScoresProvider.get(
    #             approach=Approach.QUALITY_LINEAR,
    #             protocol=Protocol.GRANDTEST,
    #             subset=subset,
    #         )
    #         for subset in Subset.options()
    #     },
    #     "Auxiliary": {
    #         subset.name: ScoresProvider.get(
    #             approach=Approach.AUXILIARY, protocol=Protocol.GRANDTEST, subset=subset
    #         )
    #         for subset in Subset.options()
    #     },
    # }
    #
    # results = {}
    # for approach, scores_subsets in approaches.items():
    #     metrics = Metrics(
    #         devel_scores=scores_subsets.get(Subset.DEVEL.name),
    #         test_scores=scores_subsets.get(Subset.TEST.name),
    #     )
    #
    #     bpcer_fixing_working_points = [0.1, 0.15, 0.20]  # [0.05, 0.1, 0.15, 0.20, 0.30, 0.40]
    #     apcer_fixing_working_points = [0.1, 0.15, 0.20]  # [0.05, 0.1, 0.15, 0.20, 0.30, 0.40]
    #
    #     analysis = metrics.get_indeepth_analysis(
    #         bpcer_fixing_working_points, apcer_fixing_working_points
    #     )
    #
    #     results[approach] = analysis

    results = {
        "Quality SVM RBF": ResultsProvider.get(
            Approach.QUALITY_RBF, Protocol.GRANDTEST
        ),
        "Quality SVM LINEAR": ResultsProvider.get(
            Approach.QUALITY_LINEAR, Protocol.GRANDTEST
        ),
        "Auxiliary": ResultsProvider.get(Approach.AUXILIARY, Protocol.GRANDTEST),
    }

    selected_working_points = {
        "APCER @ BPCER 10 %": WorkingPoint.BPCER_10,
        "APCER @ BPCER 15 %": WorkingPoint.BPCER_15,
        "APCER @ BPCER 20 %": WorkingPoint.BPCER_20,
    }
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
            "test_type_I": [
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
            ],
            "test_type_II": [
                "partial_lower_half",
                "partial_periocular",
                "partial_upper_half",
            ],
            "test_type_III": [
                "makeup_cosmetic",
                "makeup_obfuscation",
                "partial_funny_eyes",
                "partial_paper_glasses",
            ],
            "test_type_II_and_III": [
                "partial_lower_half",
                "partial_periocular",
                "partial_upper_half",
                "makeup_cosmetic",
                "makeup_obfuscation",
                "partial_funny_eyes",
                "partial_paper_glasses",
            ],
        }

        for pais_type, filter_pais in pais_group.items():
            filename = f"{output_path}/grandtest_trained_type_pai_I_{pais_type}_{working_point.value}_radar_chart.png"

            apcer_detail = create_apcer_by_pai(results, working_point, filter_pais)
            create_radar_chart_comparision(title, apcer_detail, filename)
