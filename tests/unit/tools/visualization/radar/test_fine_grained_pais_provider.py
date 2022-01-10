import pytest

from gradgpad import CombinedScenario, FineGrainedPaisProvider


@pytest.mark.unit
@pytest.mark.parametrize("combined_scenario", CombinedScenario.options())
def test_should_get_fine_grained_pais_provider(combined_scenario: CombinedScenario):
    FineGrainedPaisProvider.by(combined_scenario)
