from typing import List


class CombinedScenario:
    ALL = "All"
    PAS_I = "PAS_I"
    PAS_II = "PAS_II"
    PAS_III = "PAS_III"
    PAS_I_AND_II = "PAS_I_AND_II"
    PAS_II_AND_III = "PAS_II_AND_III"

    @staticmethod
    def options() -> List:
        return [
            CombinedScenario.ALL,
            CombinedScenario.PAS_I,
            CombinedScenario.PAS_II,
            CombinedScenario.PAS_III,
            CombinedScenario.PAS_I_AND_II,
            CombinedScenario.PAS_II_AND_III,
        ]
