import os

import pytest

from gradgpad import (
    Approach,
    BiasPercentilePlotter,
    Demographic,
    Protocol,
    ScoresProvider,
    Subset,
)


@pytest.mark.unit
@pytest.mark.parametrize("demographic", Demographic.options())
def test_should_save_a_bias_percentile_plotter(demographic: Demographic):
    os.makedirs("output", exist_ok=True)
    output_filename = "output/radar.png"
    scores = ScoresProvider.get(Approach.AUXILIARY, Protocol.GRANDTEST, Subset.TEST)
    plotter = BiasPercentilePlotter(
        title="My Title",
        demographic=demographic,
        working_point=(0.5, 0.7),
    )
    plotter.save(output_filename=output_filename, scores=scores)
    assert os.path.isfile(output_filename)
