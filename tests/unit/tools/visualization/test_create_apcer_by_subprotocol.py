import pytest

from gradgpad import Approach, ResultsProvider
from gradgpad.tools.visualization.radar.create_apcer_detail import (
    ApcerDetail,
    WorkingPoint,
    create_apcer_by_subprotocol,
)

APPROACH_RESULTS = {
    "Quality SVM RBF": ResultsProvider.all(Approach.QUALITY_RBF),
    "Quality SVM LINEAR": ResultsProvider.all(Approach.QUALITY_LINEAR),
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
def test_should_create_apcer_by_subprotocol(working_point, approach_results):
    apcer_by_pai = create_apcer_by_subprotocol(approach_results, working_point)
    assert isinstance(apcer_by_pai, ApcerDetail)
