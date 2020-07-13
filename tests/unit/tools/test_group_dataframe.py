import pytest

from gradgpad.charts import create_demographic_dataframe_comparision
from gradgpad.reproducible_research import (
    quality_results_skin_tone,
    quality_linear_results_skin_tone,
)

from gradgpad.tools import group_dataframe, Metric


@pytest.mark.unit
def test_should_group_dataframe():
    metric = Metric.BPCER
    approach_results = {
        "Quality SVM RBF": quality_results_skin_tone,
        "Quality SVM LINEAR": quality_linear_results_skin_tone,
    }
    df = create_demographic_dataframe_comparision(metric, approach_results)

    policy = {
        "Skin Tone - Yellow": [
            "Skin Tone - Light Yellow",
            "Skin Tone - Medium Yellow Brown",
        ],
        "Skin Tone - Pink": ["Skin Tone - Light Pink", "Skin Tone - Medium Pink Brown"],
        "Skin Tone - Dark Brown": [
            "Skin Tone - Medium Dark Brown",
            "Skin Tone - Dark Brown",
        ],
    }

    df = group_dataframe(df, policy)
