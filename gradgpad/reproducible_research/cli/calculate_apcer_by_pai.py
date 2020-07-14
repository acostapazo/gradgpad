from gradgpad.charts.create_radar_chart_comparision import (
    create_radar_chart_comparision,
)
from gradgpad.reproducible_research import (
    quality_results,
    quality_linear_results,
    auxiliary_results,
)
from gradgpad.tools.create_apcer_detail import WorkingPoint, create_apcer_by_pai


def calculate_apcer_by_pai(output_path: str):
    print("Calculating APCER by PAI...")

    selected_working_points = {
        "APCER @ BPCER 10 %": WorkingPoint.BPCER_10,
        "APCER @ BPCER 15 %": WorkingPoint.BPCER_15,
    }
    for title, working_point in selected_working_points.items():

        approach_results_protocol = {
            "Quality SVM RBF": quality_results["Grandtest-Type-PAI-I"],
            "Quality SVM LINEAR": quality_linear_results["Grandtest-Type-PAI-I"],
            "Auxiliary": auxiliary_results["Grandtest-Type-PAI-I"],
        }
        filename = f"{output_path}/grandtest_trained_type_pai_I_{working_point.value}_radar_chart.png"
        discard_pais = None

        apcer_detail = create_apcer_by_pai(
            approach_results_protocol, working_point, discard_pais
        )
        create_radar_chart_comparision(title, apcer_detail, filename)
