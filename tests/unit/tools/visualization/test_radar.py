import os

import pytest

from gradgpad import (
    ResultsProvider,
    Approach,
    ConfigRadar,
    Radar,
    WorkingPoint,
    Protocol,
)
from gradgpad.tools.visualization.radar.fine_grained_pais_provider import (
    FineGrainedPaisProvider,
)

APPROACH_RESULTS = {
    "Quality SVM RBF": ResultsProvider.get(
        Approach.QUALITY_RBF, protocol=Protocol.GRANDTEST
    ),
    "Auxiliary": ResultsProvider.get(Approach.AUXILIARY, protocol=Protocol.GRANDTEST),
}


@pytest.mark.unit
@pytest.mark.parametrize(
    "working_point,approach_results",
    [
        (WorkingPoint.BPCER_5, APPROACH_RESULTS),
        (WorkingPoint.BPCER_10, APPROACH_RESULTS),
    ],
)
def test_should_save_a_radar(working_point, approach_results):
    output_filename = "output/radar.png"
    config_radar = ConfigRadar(
        title="My Title",
        working_point=working_point,
        filter_pais=FineGrainedPaisProvider.pas_I_and_II(),
    )
    radar = Radar(config_radar)
    radar.save(output_filename=output_filename, results=approach_results)

    assert os.path.isfile(output_filename)
