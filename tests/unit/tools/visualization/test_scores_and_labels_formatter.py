import pytest

from gradgpad import Approach, Protocol, ScoresProvider, SplitByLabelMode, Subset
from gradgpad.tools.visualization.scores_and_labels_formatter import (
    ScoresAndLabelsFormatter,
)


@pytest.mark.unit
@pytest.mark.parametrize("split_by_label_mode", SplitByLabelMode.options())
def test_should_execute_a_scores_and_labels_formatter(
    split_by_label_mode: SplitByLabelMode,
):
    scores = ScoresProvider.get(Approach.AUXILIARY, Protocol.GRANDTEST, Subset.TEST)
    ScoresAndLabelsFormatter.execute(scores, split_by_label_mode)
