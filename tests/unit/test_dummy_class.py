from __future__ import absolute_import

import pytest
from meiga.assertions import assert_success, assert_failure
from meiga import Error

from gradgpad.example.dummy_class import DummyCalculator


@pytest.mark.unit
def test_should_sum_up_given_values(given_any_number_tuple):
    calculator = DummyCalculator(given_any_number_tuple[0], given_any_number_tuple[1])
    result = calculator.sum()
    assert_success(result, value_is_instance_of=int)


@pytest.mark.unit
def test_should_return_error_when_dividing_by_zero(given_zero_tuple):
    calculator = DummyCalculator(given_zero_tuple[0], given_zero_tuple[1])
    result = calculator.divide()
    assert_failure(result, value_is_instance_of=Error)
