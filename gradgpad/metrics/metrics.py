from gradgpad.metrics.eer import eer
from gradgpad.reproducible_research import Scores


class Metrics:
    def __init__(self, devel_scores: Scores, test_scores: Scores):
        self.devel_scores = devel_scores
        self.test_scores = test_scores

    def get_eer_devel(self):
        eer_value, _ = eer(
            self.devel_scores.get_numpy_scores(), self.devel_scores.get_numpy_labels()
        )
        return eer_value

    def get_eer_test(self):
        eer_value, _ = eer(
            self.devel_scores.get_numpy_scores(), self.devel_scores.get_numpy_labels()
        )
        return eer_value
