import os

import pytest

from gradgpad import (
    Approach,
    HistogramPlotter,
    Protocol,
    ScoresProvider,
    SplitByLabelMode,
    Subset,
)


@pytest.mark.unit
@pytest.mark.parametrize("split_by_label_mode", SplitByLabelMode.options_for_curves())
def test_should_save_a_histogram_plotter(split_by_label_mode: SplitByLabelMode):
    os.makedirs("output", exist_ok=True)
    output_filename = "output/radar.png"
    scores = ScoresProvider.get(Approach.AUXILIARY, Protocol.GRANDTEST, Subset.TEST)
    plotter = HistogramPlotter(
        title="My Title",
        split_by_label_mode=split_by_label_mode,
    )
    plotter.save(output_filename=output_filename, scores=scores)
    assert os.path.isfile(output_filename)


@pytest.mark.unit
def test_should_raise_a_io_error_when_save_a_histogram_plotter_with_no_valid_output_filename():
    plotter = HistogramPlotter(
        title="My Title",
        split_by_label_mode=SplitByLabelMode.DATASET,
    )
    pytest.raises(
        IOError,
        lambda: plotter.save(output_filename="not_valid_folder/name", scores=None),
    )
