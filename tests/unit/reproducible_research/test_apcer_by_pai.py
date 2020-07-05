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


@pytest.mark.unit
@pytest.mark.parametrize(
    "title,working_point,approach_results_protocol, filename",
    [
        (
            "APCER @ BPCER 5 %",
            WorkingPoint.BPCER_5,
            {
                "Quality SVM RVC": quality_results["Grandtest-Type-PAI-I"],
                "Quality SVM LINEAR": quality_linear_results["Grandtest-Type-PAI-I"],
                "Auxiliary": auxiliary_results["Grandtest-Type-PAI-I"],
            },
            "tests/output/grandtest_type_pai_I_apcer_by_pai_fixing_wp_bpcer_5_radar_chart.png",
        ),
        (
            "APCER @ BPCER 10 %",
            WorkingPoint.BPCER_10,
            {
                "Quality SVM RVC": quality_results["Grandtest-Type-PAI-I"],
                "Quality SVM LINEAR": quality_linear_results["Grandtest-Type-PAI-I"],
                "Auxiliary": auxiliary_results["Grandtest-Type-PAI-I"],
            },
            "tests/output/grandtest_type_pai_I_apcer_by_pai_fixing_wp_bpcer_10_radar_chart.png",
        ),
        (
            "APCER @ BPCER 15 %",
            WorkingPoint.BPCER_15,
            {
                "Quality SVM RVC": quality_results["Grandtest-Type-PAI-I"],
                "Quality SVM LINEAR": quality_linear_results["Grandtest-Type-PAI-I"],
                "Auxiliary": auxiliary_results["Grandtest-Type-PAI-I"],
            },
            "tests/output/grandtest_type_pai_I_apcer_by_pai_fixing_wp_bpcer_15_radar_chart.png",
        ),
        (
            "APCER @ BPCER 5 %",
            WorkingPoint.BPCER_5,
            {
                "Quality SVM RVC": quality_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Quality SVM LINEAR": quality_linear_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Auxiliary": auxiliary_results["Grandtest-Train-Type-PAI-I-Test-All"],
            },
            "tests/output/grandtest_type_pai_I_test_all_apcer_by_pai_fixing_wp_bpcer_5_radar_chart.png",
        ),
        (
            "APCER @ BPCER 10 %",
            WorkingPoint.BPCER_10,
            {
                "Quality SVM RVC": quality_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Quality SVM LINEAR": quality_linear_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Auxiliary": auxiliary_results["Grandtest-Train-Type-PAI-I-Test-All"],
            },
            "tests/output/grandtest_type_pai_I_test_all_apcer_by_pai_fixing_wp_bpcer_10_radar_chart.png",
        ),
        (
            "APCER @ BPCER 15 %",
            WorkingPoint.BPCER_15,
            {
                "Quality SVM RVC": quality_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Quality SVM LINEAR": quality_linear_results[
                    "Grandtest-Train-Type-PAI-I-Test-All"
                ],
                "Auxiliary": auxiliary_results["Grandtest-Train-Type-PAI-I-Test-All"],
            },
            "tests/output/grandtest_type_pai_I_test_all_apcer_by_pai_fixing_wp_bpcer_15_radar_chart.png",
        ),
    ],
)
def test_should_create_apcer_by_pai_radar_chart_comparision(
    title, working_point, approach_results_protocol, filename
):
    apcer_detail = create_apcer_by_pai(approach_results_protocol, working_point)
    create_radar_chart_comparision(title, apcer_detail, filename)
