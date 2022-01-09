import pytest

from gradgpad import Approach, ResultsProvider
from gradgpad.tools.visualization.radar.create_apcer_detail import (
    ApcerDetail,
    WorkingPoint,
    create_apcer_by_pai,
)

APPROACH_RESULTS_GRANDTEST = {
    "Quality SVM RBF": ResultsProvider.grandtest(Approach.QUALITY_RBF)["grandtest"],
    "Quality SVM LINEAR": ResultsProvider.grandtest(Approach.QUALITY_LINEAR)[
        "grandtest"
    ],
    "Auxiliary": ResultsProvider.grandtest(Approach.AUXILIARY)["grandtest"],
}


@pytest.mark.unit
@pytest.mark.parametrize(
    "working_point,approach_results_protocol",
    [
        (WorkingPoint.BPCER_5, APPROACH_RESULTS_GRANDTEST),
        (WorkingPoint.BPCER_10, APPROACH_RESULTS_GRANDTEST),
    ],
)
def test_should_create_apcer_by_pai(working_point, approach_results_protocol):

    apcer_by_pai = create_apcer_by_pai(approach_results_protocol, working_point)
    assert isinstance(apcer_by_pai, ApcerDetail)
