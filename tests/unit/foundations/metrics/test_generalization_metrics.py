import os

import pytest

from gradgpad import Approach, GeneralizationMetrics, ResultsProvider


@pytest.mark.unit
@pytest.mark.skip
def test_should_save_generalization_metrics():
    os.makedirs("output", exist_ok=True)
    output_filename = "output/generalization_metrics.txt"
    all_results = ResultsProvider.all(Approach.AUXILIARY)
    generalization_metrics = GeneralizationMetrics()
    generalization_metrics.save(
        output_filename=output_filename, all_results=all_results
    )

    assert os.path.isfile(output_filename)
