import pytest

from gradgpad.foundations.results import ResultsProvider
from gradgpad.foundations.scores import Approach


def check_all_values(nested_dictionary):
    for key, value in nested_dictionary.items():
        if type(value) is dict:
            check_all_values(value)
        else:
            # print(key, ":", value)
            if isinstance(value, float):
                assert value >= 0.0, f"{key} is negative ({value})"
                assert value <= 100.0, f"{key} is larger than 100 ({value})"


@pytest.mark.unit
@pytest.mark.parametrize(
    "approach",
    Approach.options_excluding(
        [Approach.QUALITY_RBF_BALANCED, Approach.CONTINUAL_LEARNING_AUXILIARY]
    ),
)
def test_should_check_results_are_ok(approach: Approach):

    results = ResultsProvider.all(approach)
    check_all_values(results)
