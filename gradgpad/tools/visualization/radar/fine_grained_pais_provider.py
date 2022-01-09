from typing import List

from gradgpad.tools.visualization.radar.combined_scenario import CombinedScenario


class FineGrainedPaisProvider:
    @staticmethod
    def by(combined_scenario: CombinedScenario):
        if combined_scenario == CombinedScenario.ALL:
            return FineGrainedPaisProvider.all()
        elif combined_scenario == CombinedScenario.PAS_I:
            return FineGrainedPaisProvider.pas_I()
        elif combined_scenario == CombinedScenario.PAS_II:
            return FineGrainedPaisProvider.pas_II()
        elif combined_scenario == CombinedScenario.PAS_III:
            return FineGrainedPaisProvider.pas_III()
        elif combined_scenario == CombinedScenario.PAS_I_AND_II:
            return FineGrainedPaisProvider.pas_I_and_II()
        elif combined_scenario == CombinedScenario.PAS_II_AND_III:
            return FineGrainedPaisProvider.pas_II_and_III()

    @staticmethod
    def all() -> List[str]:
        return [
            "print_low_quality",
            "print_medium_quality",
            "print_high_quality",
            "replay_low_quality",
            "replay_medium_quality",
            "replay_high_quality",
            "mask_paper",
            "mask_rigid",
            "mask_silicone",
            "makeup_impersonation",
            "partial_lower_half",
            "partial_periocular",
            "partial_upper_half",
            "makeup_cosmetic",
            "makeup_obfuscation",
            "partial_funny_eyes",
            "partial_paper_glasses",
        ]

    @staticmethod
    def pas_I() -> List[str]:
        return [
            "print_low_quality",
            "print_medium_quality",
            "print_high_quality",
            "replay_low_quality",
            "replay_medium_quality",
            "replay_high_quality",
            "mask_paper",
            "mask_rigid",
            "mask_silicone",
            "makeup_impersonation",
        ]

    @staticmethod
    def pas_I_and_II() -> List[str]:
        return [
            "print_low_quality",
            "print_medium_quality",
            "print_high_quality",
            "replay_low_quality",
            "replay_medium_quality",
            "replay_high_quality",
            "mask_paper",
            "mask_rigid",
            "mask_silicone",
            "makeup_impersonation",
            "partial_lower_half",
            "partial_periocular",
            "partial_upper_half",
        ]

    @staticmethod
    def pas_II() -> List[str]:
        return ["partial_lower_half", "partial_periocular", "partial_upper_half"]

    @staticmethod
    def pas_III() -> List[str]:
        return [
            "makeup_cosmetic",
            "makeup_obfuscation",
            "partial_funny_eyes",
            "partial_paper_glasses",
        ]

    @staticmethod
    def pas_II_and_III() -> List[str]:
        return [
            "partial_lower_half",
            "partial_periocular",
            "partial_upper_half",
            "makeup_cosmetic",
            "makeup_obfuscation",
            "partial_funny_eyes",
            "partial_paper_glasses",
        ]
