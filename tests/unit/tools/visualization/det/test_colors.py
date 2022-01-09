import pytest

from gradgpad.tools.visualization.colors import get_color_random_style


@pytest.mark.unit
def test_should_obtain_a_random_color_style():
    color, linestyles, markers = get_color_random_style()
    assert isinstance(color, str)
    assert isinstance(linestyles, str)
    assert isinstance(markers, str)
