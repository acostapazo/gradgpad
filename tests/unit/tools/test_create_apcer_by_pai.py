import pytest

from gradgpad.reproducible_research import quality_results, quality_linear_results
from gradgpad.tools.create_apcer_detail import (
    WorkingPoint,
    create_apcer_by_pai,
    ApcerDetail,
)


@pytest.mark.unit
@pytest.mark.parametrize(
    "working_point,approach_results_protocol",
    [
        (
            WorkingPoint.BPCER_5,
            {
                "Quality SVM RBF": quality_results["Grandtest-Type-PAI-I"],
                "Quality SVM LINEAR": quality_linear_results["Grandtest-Type-PAI-I"],
            },
        ),
        (
            WorkingPoint.BPCER_10,
            {
                "Quality SVM RBF": quality_results["Grandtest-Type-PAI-I"],
                "Quality SVM LINEAR": quality_linear_results["Grandtest-Type-PAI-I"],
            },
        ),
    ],
)
def test_should_create_apcer_by_pai(working_point, approach_results_protocol):

    apcer_by_pai = create_apcer_by_pai(approach_results_protocol, working_point)
    assert isinstance(apcer_by_pai, ApcerDetail)
