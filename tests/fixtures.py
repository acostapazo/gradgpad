import pytest


@pytest.fixture
def given_any_number_tuple():
    return 3, 5


@pytest.fixture
def given_zero_tuple():
    return 0, 0
