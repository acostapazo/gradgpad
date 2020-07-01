import pytest

from gradgpad.charts.create_radar_chart_comparision import (
    create_radar_chart_comparision,
)
from gradgpad.reproducible_research import (
    quality_results_cross_dataset,
    quality_linear_results_cross_dataset,
    quality_results_lodo,
    quality_linear_results_lodo,
    quality_results_cross_device,
    quality_linear_results_cross_device,
    quality_results_unseen_attack,
    quality_linear_results_unseen_attack,
)
from gradgpad.tools.create_apcer_detail import WorkingPoint, create_apcer_by_subprotocol


@pytest.mark.unit
@pytest.mark.parametrize(
    "title,working_point,approach_results_protocol,filter_common,filename",
    [
        (
            "Cross-Dataset - APCER @ BPCER 5 %",
            WorkingPoint.BPCER_5,
            {
                "Quality SVM RVC": quality_results_cross_dataset,
                "Quality SVM LINEAR": quality_linear_results_cross_dataset,
            },
            "Cross-Dataset - ",
            "tests/output/cross_dataset_apcer_fixing_wp_bpcer_5_radar_chart.png",
        ),
        (
            "Cross-Dataset - APCER @ BPCER 10 %",
            WorkingPoint.BPCER_10,
            {
                "Quality SVM RVC": quality_results_cross_dataset,
                "Quality SVM LINEAR": quality_linear_results_cross_dataset,
            },
            "Cross-Dataset - ",
            "tests/output/cross_dataset_apcer_fixing_wp_bpcer_10_radar_chart.png",
        ),
        (
            "Cross-Dataset - APCER @ BPCER 15 %",
            WorkingPoint.BPCER_15,
            {
                "Quality SVM RVC": quality_results_cross_dataset,
                "Quality SVM LINEAR": quality_linear_results_cross_dataset,
            },
            "Cross-Dataset - ",
            "tests/output/cross_dataset_apcer_fixing_wp_bpcer_15_radar_chart.png",
        ),
        (
            "LODO - APCER @ BPCER 5 %",
            WorkingPoint.BPCER_5,
            {
                "Quality SVM RVC": quality_results_lodo,
                "Quality SVM LINEAR": quality_linear_results_lodo,
            },
            "LODO - ",
            "tests/output/lodo_apcer_fixing_wp_bpcer_5_radar_chart.png",
        ),
        (
            "LODO - APCER @ BPCER 10 %",
            WorkingPoint.BPCER_10,
            {
                "Quality SVM RVC": quality_results_lodo,
                "Quality SVM LINEAR": quality_linear_results_lodo,
            },
            "LODO - ",
            "tests/output/lodo_apcer_fixing_wp_bpcer_10_radar_chart.png",
        ),
        (
            "LODO - APCER @ BPCER 15 %",
            WorkingPoint.BPCER_15,
            {
                "Quality SVM RVC": quality_results_cross_dataset,
                "Quality SVM LINEAR": quality_linear_results_cross_dataset,
            },
            "LODO - ",
            "tests/output/lodo_apcer_fixing_wp_bpcer_15_radar_chart.png",
        ),
        (
            "Cross-Device - APCER @ BPCER 5 %",
            WorkingPoint.BPCER_5,
            {
                "Quality SVM RVC": quality_results_cross_device,
                "Quality SVM LINEAR": quality_linear_results_cross_device,
            },
            "Cross-Device - ",
            "tests/output/cross_device_apcer_fixing_wp_bpcer_5_radar_chart.png",
        ),
        (
            "Cross-Device - APCER @ BPCER 10 %",
            WorkingPoint.BPCER_10,
            {
                "Quality SVM RVC": quality_results_cross_device,
                "Quality SVM LINEAR": quality_linear_results_cross_device,
            },
            "Cross-Device - ",
            "tests/output/cross_device_apcer_fixing_wp_bpcer_10_radar_chart.png",
        ),
        (
            "Cross-Device - APCER @ BPCER 15 %",
            WorkingPoint.BPCER_15,
            {
                "Quality SVM RVC": quality_results_cross_device,
                "Quality SVM LINEAR": quality_linear_results_cross_device,
            },
            "Cross-Device - ",
            "tests/output/cross_device_apcer_fixing_wp_bpcer_15_radar_chart.png",
        ),
        (
            "Unseen-Attack - APCER @ BPCER 5 %",
            WorkingPoint.BPCER_5,
            {
                "Quality SVM RVC": quality_results_unseen_attack,
                "Quality SVM LINEAR": quality_linear_results_unseen_attack,
            },
            "Unseen-Attack - ",
            "tests/output/unseen_attack_apcer_fixing_wp_bpcer_5_radar_chart.png",
        ),
        (
            "Unseen-Attack - APCER @ BPCER 10 %",
            WorkingPoint.BPCER_10,
            {
                "Quality SVM RVC": quality_results_unseen_attack,
                "Quality SVM LINEAR": quality_linear_results_unseen_attack,
            },
            "Unseen-Attack - ",
            "tests/output/unseen_attack_apcer_fixing_wp_bpcer_10_radar_chart.png",
        ),
        (
            "Unseen-Attack - APCER @ BPCER 15 %",
            WorkingPoint.BPCER_15,
            {
                "Quality SVM RVC": quality_results_unseen_attack,
                "Quality SVM LINEAR": quality_linear_results_unseen_attack,
            },
            "Unseen-Attack - ",
            "tests/output/unseen_attack_apcer_fixing_wp_bpcer_15_radar_chart.png",
        ),
    ],
)
def test_should_create_apcer_by_subprotocol_radar_chart_comparision(
    title, working_point, approach_results_protocol, filter_common, filename
):
    apcer_detail = create_apcer_by_subprotocol(
        approach_results_protocol, working_point, filter_common
    )
    create_radar_chart_comparision(title, apcer_detail, filename)
