import pytest

from gradgpad.reproducible_research import (
    quality_results_cross_dataset,
    quality_linear_results_cross_dataset,
)
from gradgpad.tools.create_apcer_detail import (
    WorkingPoint,
    ApcerDetail,
    create_apcer_by_subprotocol,
)


@pytest.mark.unit
@pytest.mark.parametrize(
    "working_point,approach_results",
    [
        (
            WorkingPoint.BPCER_5,
            {
                "Quality SVM RBF": quality_results_cross_dataset,
                "Quality SVM LINEAR": quality_linear_results_cross_dataset,
            },
        ),
        (
            WorkingPoint.BPCER_10,
            {
                "Quality SVM RBF": quality_results_cross_dataset,
                "Quality SVM LINEAR": quality_linear_results_cross_dataset,
            },
        ),
    ],
)
def test_should_create_apcer_by_subprotocol(working_point, approach_results):
    apcer_by_pai = create_apcer_by_subprotocol(approach_results, working_point)
    assert isinstance(apcer_by_pai, ApcerDetail)
