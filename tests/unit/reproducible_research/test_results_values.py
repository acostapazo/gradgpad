import pytest


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
def test_should_check_quality_results_are_ok():
    from gradgpad.reproducible_research import quality_results

    check_all_values(quality_results)


@pytest.mark.unit
def test_should_check_quality_linear_results_are_ok():
    from gradgpad.reproducible_research import quality_linear_results

    check_all_values(quality_linear_results)


@pytest.mark.unit
def test_should_check_auxiliary_results_are_ok():
    from gradgpad.reproducible_research import auxiliary_results

    check_all_values(auxiliary_results)
