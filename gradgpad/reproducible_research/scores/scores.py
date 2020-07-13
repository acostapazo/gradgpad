import os

from gradgpad.annotations.filter import Filter
from gradgpad.tools.open_result_json import open_result_json
from gradgpad import annotations

REPRODUCIBLE_RESEARCH_SCORES_DIR = os.path.abspath(os.path.dirname(__file__))


class Scores:
    def __init__(self, filename):
        self.scores = open_result_json(filename)

    def filtered_by(self, filter: Filter):
        ids = annotations.get_ids(filter)
        return {key: value for key, value in self.scores.items() if key in ids}

    def length(self):
        return len(self.scores)


quality_rbf_scores_grandtest_type_I = Scores(
    f"{REPRODUCIBLE_RESEARCH_SCORES_DIR}/quality_rbf/quality-rbf-Grandtest-Type-PAI-I-test.json"
)

quality_linear_scores_grandtest_type_I = Scores(
    f"{REPRODUCIBLE_RESEARCH_SCORES_DIR}/quality_linear/quality-linear-Grandtest-Type-PAI-I-test.json"
)
