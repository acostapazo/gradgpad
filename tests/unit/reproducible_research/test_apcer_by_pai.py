import pytest

from gradgpad.charts.create_radar_chart_comparision import (
    create_radar_chart_comparision,
)
from gradgpad.reproducible_research import (
    quality_results,
    quality_linear_results,
    auxiliary_results,
)
from gradgpad.tools.create_apcer_detail import WorkingPoint, create_apcer_by_pai

PAIS_TYPE_I = [
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
]


@pytest.mark.unit
@pytest.mark.parametrize(
    "title,working_point,approach_results_protocol,filename,discard_pais",
    [
        (
            "APCER @ BPCER 5 %",
            WorkingPoint.BPCER_5,
            {
                "Quality SVM RBF": quality_results["Grandtest-Type-PAI-I"],
                "Quality SVM LINEAR": quality_linear_results["Grandtest-Type-PAI-I"],
                "Auxiliary": auxiliary_results["Grandtest-Type-PAI-I"],
            },
            "tests/output/grandtest_type_pai_I_apcer_by_pai_fixing_wp_bpcer_5_radar_chart.png",
            None,
        ),
        (
            "APCER @ BPCER 10 %",
            WorkingPoint.BPCER_10,
            {
                "Quality SVM RBF": quality_results["Grandtest-Type-PAI-I"],
                "Quality SVM LINEAR": quality_linear_results["Grandtest-Type-PAI-I"],
                "Auxiliary": auxiliary_results["Grandtest-Type-PAI-I"],
            },
            "tests/output/grandtest_type_pai_I_apcer_by_pai_fixing_wp_bpcer_10_radar_chart.png",
            None,
        ),
        (
            "APCER @ BPCER 15 %",
            WorkingPoint.BPCER_15,
            {
                "Quality SVM RBF": quality_results["Grandtest-Type-PAI-I"],
                "Quality SVM LINEAR": quality_linear_results["Grandtest-Type-PAI-I"],
                "Auxiliary": auxiliary_results["Grandtest-Type-PAI-I"],
            },
            "tests/output/grandtest_type_pai_I_apcer_by_pai_fixing_wp_bpcer_15_radar_chart.png",
            None,
        ),
        (
            "APCER @ BPCER 5 %",
            WorkingPoint.BPCER_5,
            {
                "Quality SVM RBF": quality_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Quality SVM LINEAR": quality_linear_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Auxiliary": auxiliary_results["Grandtest-Train-Type-PAI-I-Test-All"],
            },
            "tests/output/grandtest_type_pai_II_apcer_by_pai_fixing_wp_bpcer_5_radar_chart.png",
            PAIS_TYPE_I,
        ),
        (
            "APCER @ BPCER 10 %",
            WorkingPoint.BPCER_10,
            {
                "Quality SVM RBF": quality_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Quality SVM LINEAR": quality_linear_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Auxiliary": auxiliary_results["Grandtest-Train-Type-PAI-I-Test-All"],
            },
            "tests/output/grandtest_type_pai_II_apcer_by_pai_fixing_wp_bpcer_10_radar_chart.png",
            PAIS_TYPE_I,
        ),
        (
            "APCER @ BPCER 15 %",
            WorkingPoint.BPCER_15,
            {
                "Quality SVM RBF": quality_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Quality SVM LINEAR": quality_linear_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Auxiliary": auxiliary_results["Grandtest-Train-Type-PAI-I-Test-All"],
            },
            "tests/output/grandtest_type_pai_II_apcer_by_pai_fixing_wp_bpcer_15_radar_chart.png",
            PAIS_TYPE_I,
        ),
    ],
)
def test_should_create_apcer_by_pai_radar_chart_comparision(
    title, working_point, approach_results_protocol, filename, discard_pais
):
    apcer_detail = create_apcer_by_pai(
        approach_results_protocol, working_point, discard_pais
    )
    create_radar_chart_comparision(title, apcer_detail, filename)
