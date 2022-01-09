import os

import pytest

from gradgpad import (
    Approach,
    DetPlotter,
    Protocol,
    ScoresProvider,
    SplitByLabelMode,
    Subset,
)


@pytest.mark.unit
@pytest.mark.parametrize("split_by_label_mode", SplitByLabelMode.options_for_curves())
def test_should_save_a_det_plotter(split_by_label_mode: SplitByLabelMode):
    os.makedirs("output", exist_ok=True)
    output_filename = "output/radar.png"
    scores = ScoresProvider.get(Approach.AUXILIARY, Protocol.GRANDTEST, Subset.TEST)
    plotter = DetPlotter(
        title="My Title",
        split_by_label_mode=split_by_label_mode,
    )
    plotter.save(output_filename=output_filename, scores=scores)
    assert os.path.isfile(output_filename)


@pytest.mark.unit
def test_should_raise_a_type_error_when_save_a_det_plotter_with_no_valid_split_by_label_mode():
    pytest.raises(
        TypeError,
        lambda: DetPlotter(
            title="My Title",
            split_by_label_mode=SplitByLabelMode.DATASET,
        ),
    )
