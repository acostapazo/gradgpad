import pytest

from gradgpad.annotations.stats.calculate_pai_stats import calculate_pai_stats


@pytest.mark.unit
def test_should_load_annotations():
    from gradgpad import annotations

    assert annotations.num_annotations == 29567


@pytest.mark.unit
def test_should_calculate_pai_stats():
    from gradgpad import annotations

    pai_stats = calculate_pai_stats(annotations)

    assert list(pai_stats.keys()) == [
        "num_genuines",
        "num_attacks",
        "num_type_pai",
        "num_coarse_grained_pai",
        "num_fine_grained_pai",
        "percentage_num_type_pai",
        "percentage_num_coarse_grained_pai",
        "percentage_num_fine_grained_pai",
    ]
