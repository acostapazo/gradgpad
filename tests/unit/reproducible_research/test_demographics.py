import pytest
from pandas import DataFrame

from gradgpad.charts import create_metric_bar_chart_comparision
from gradgpad.reproducible_research import (
    quality_results_gender,
    quality_linear_results_gender,
    quality_results_age,
    quality_linear_results_age,
    quality_linear_results_skin_tone,
    quality_results_skin_tone,
)
from gradgpad.reproducible_research.demographic import (
    create_demographic_dataframe_comparision,
)
from gradgpad.tools import group_dataframe, Metric


@pytest.mark.unit
@pytest.mark.parametrize(
    "metric,approach_results,filename",
    [
        (
            Metric.BPCER,
            {
                "Quality SVM RVC": quality_results_gender,
                "Quality SVM LINEAR": quality_linear_results_gender,
            },
            "tests/output/gender_bpcer_comparision_bar_chart.png",
        ),
        (
            Metric.BPCER,
            {
                "Quality SVM RVC": quality_results_age,
                "Quality SVM LINEAR": quality_linear_results_age,
            },
            "tests/output/age_bpcer_comparision_bar_chart.png",
        ),
        (
            Metric.BPCER,
            {
                "Quality SVM RVC": quality_results_skin_tone,
                "Quality SVM LINEAR": quality_linear_results_skin_tone,
            },
            "tests/output/skin_tone_bpcer_comparision_bar_chart.png",
        ),
        (
            Metric.APCER_AGGREGATE,
            {
                "Quality SVM RVC": quality_results_gender,
                "Quality SVM LINEAR": quality_linear_results_gender,
            },
            "tests/output/gender_apcer_aggregate_comparision_bar_chart.png",
        ),
        (
            Metric.APCER_AGGREGATE,
            {
                "Quality SVM RVC": quality_results_age,
                "Quality SVM LINEAR": quality_linear_results_age,
            },
            "tests/output/age_apcer_aggregate_comparision_bar_chart.png",
        ),
        (
            Metric.APCER_AGGREGATE,
            {
                "Quality SVM RVC": quality_results_skin_tone,
                "Quality SVM LINEAR": quality_linear_results_skin_tone,
            },
            "tests/output/skin_tone_apcer_aggregate_comparision_bar_chart.png",
        ),
        (
            Metric.APCER_SPECIFIC,
            {
                "Quality SVM RVC": quality_results_gender,
                "Quality SVM LINEAR": quality_linear_results_gender,
            },
            "tests/output/gender_apcer_specific_comparision_bar_chart.png",
        ),
        (
            Metric.APCER_SPECIFIC,
            {
                "Quality SVM RVC": quality_results_age,
                "Quality SVM LINEAR": quality_linear_results_age,
            },
            "tests/output/age_apcer_specific_comparision_bar_chart.png",
        ),
        (
            Metric.APCER_AGGREGATE,
            {
                "Quality SVM RVC": quality_results_skin_tone,
                "Quality SVM LINEAR": quality_linear_results_skin_tone,
            },
            "tests/output/skin_tone_apcer_specific_comparision_bar_chart.png",
        ),
    ],
)
def test_should_create_demographic_df_and_comparision_bar_chart(
    metric, approach_results, filename
):

    df = create_demographic_dataframe_comparision(metric, approach_results)
    assert isinstance(df, DataFrame)

    create_metric_bar_chart_comparision(df, filename)


@pytest.mark.unit
@pytest.mark.parametrize(
    "metric,approach_results,policy,filename",
    [
        (
            Metric.BPCER,
            {
                "Quality SVM RVC": quality_results_skin_tone,
                "Quality SVM LINEAR": quality_linear_results_skin_tone,
            },
            {
                "Skin Tone - Yellow": [
                    "Skin Tone - Light Yellow",
                    "Skin Tone - Medium Yellow Brown",
                ],
                "Skin Tone - Pink": [
                    "Skin Tone - Light Pink",
                    "Skin Tone - Medium Pink Brown",
                ],
                "Skin Tone - Dark Brown": [
                    "Skin Tone - Medium Dark Brown",
                    "Skin Tone - Dark Brown",
                ],
            },
            "tests/output/skin_tone_grouped_comparision_bar_chart.png",
        )
    ],
)
def test_should_create_grouped_demographic_df_and_comparision_bar_chart(
    metric, approach_results, policy, filename
):

    df = create_demographic_dataframe_comparision(metric, approach_results)
    df = group_dataframe(df, policy)

    create_metric_bar_chart_comparision(df, filename)
