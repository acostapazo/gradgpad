import pytest
from pandas import DataFrame

from gradgpad.reproducible_research import quality_results_gender
from gradgpad.tools import create_dataframe, bpcer_metric_retriever


@pytest.mark.unit
def test_should_create_dataframe():
    df = create_dataframe(bpcer_metric_retriever, quality_results_gender)
    assert isinstance(df, DataFrame)
