import numpy as np
from gradgpad.foundations.metrics.bpcer import bpcer
from gradgpad.foundations.metrics.eer import eer

from gradgpad.reproducible_research import Scores, Callable, Dict


class MetricsDemographics:
    @staticmethod
    def from_subset_scores(subset_scores: Dict[str, Scores]):
        return MetricsDemographics(subset_scores["devel"], subset_scores["test"])

    def __init__(self, devel_scores: Scores, test_scores: Scores):
        self.devel_scores = devel_scores
        self.test_scores = test_scores

    def get_bpcer_age(self):
        def age_subsets_provider():
            return self.test_scores.get_fair_age_subset()

        return self._get_bpcer(age_subsets_provider)

    def get_bpcer_sex(self):
        def sex_subsets_provider():
            return self.test_scores.get_fair_sex_subset()

        return self._get_bpcer(sex_subsets_provider)

    def get_bpcer_skin_tone(self):
        def skin_tone_subsets_provider():
            return self.test_scores.get_fair_skin_tone_subset()

        return self._get_bpcer(skin_tone_subsets_provider)

    def _get_bpcer(self, subsets_provider: Callable):
        _, eer_th = eer(
            self.devel_scores.get_numpy_scores(), self.devel_scores.get_numpy_labels()
        )

        subset_scores = subsets_provider()

        bpcers = {}
        for demographic, scores in subset_scores.items():
            demographic_scores = np.asarray(list(scores.values()), dtype=np.float32)
            labels = np.asarray([0] * len(demographic_scores), dtype=np.int)
            bpcers[demographic] = bpcer(demographic_scores, labels, eer_th) * 100.0

        return bpcers
