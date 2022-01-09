import os

import pytest

from gradgpad import (
    Approach,
    GrainedPaiMode,
    PadRadarProtocolPlotter,
    Protocol,
    ResultsProvider,
    WorkingPoint,
)

APPROACH_RESULTS = {
    "Quality SVM RBF": ResultsProvider.all(Approach.QUALITY_RBF),
    "Auxiliary": ResultsProvider.all(Approach.AUXILIARY),
}


@pytest.mark.unit
@pytest.mark.parametrize(
    "working_point,approach_results",
    [
        (WorkingPoint.BPCER_5, APPROACH_RESULTS),
        (WorkingPoint.BPCER_10, APPROACH_RESULTS),
    ],
)
def test_should_save_a_pad_radar_protocol_plotter(working_point, approach_results):
    os.makedirs("output", exist_ok=True)
    output_filename = "output/radar.png"
    radar = PadRadarProtocolPlotter(
        title="My Title",
        working_point=working_point,
        grained_pai_mode=GrainedPaiMode.FINE,
        protocol=Protocol.CROSS_DATASET,
    )
    radar.save(output_filename=output_filename, results=approach_results)

    assert os.path.isfile(output_filename)
