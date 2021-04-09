import os
import time
import warnings

from gradgpad.reproducible_research.cli.calculate_pad_radar_by_generalization_protocols import (
    calculate_pad_radar_by_generalization_protocols,
)
from gradgpad.reproducible_research.cli.calculate_demographic_bpcer_bar_chart import (
    calculate_demographic_bpcer_bar_chart,
)
from gradgpad.reproducible_research.cli.calculate_demographic_percentil_based_metric import (
    calculate_demographic_percentile_based_metric,
)
from gradgpad.reproducible_research.cli.calculate_demographic_percentile_comparison import (
    calculate_demographic_percentile_comparison,
)
from gradgpad.reproducible_research.cli.calculate_hists_and_curves import (
    calculate_hists_and_curves,
)
from gradgpad.reproducible_research.cli.calculate_pad_radar_by_pai import (
    calculate_pad_radar_by_pai,
)
from gradgpad.reproducible_research.cli.summary_table import summary_table
from gradgpad.foundations.scores.protocol import Protocol


def reproducible_research(output_path: str):
    start = time.time()

    os.makedirs(output_path, exist_ok=True)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        # Classical Experiments
        summary_table(output_path)
        calculate_hists_and_curves(output_path, only_grandtest=True)

        # Novel proposals
        calculate_pad_radar_by_pai(output_path)
        calculate_pad_radar_by_generalization_protocols(output_path)

        # Demographic Experiments
        calculate_demographic_bpcer_bar_chart(output_path)
        calculate_demographic_percentile_based_metric(
            output_path, protocol=Protocol.GRANDTEST
        )
        calculate_demographic_percentile_comparison(
            output_path,
            protocol_left=Protocol.GRANDTEST,
            protocol_right=Protocol.GRANDTEST_SEX_50_50,
            title_left="Auxiliary\n GRAD-GPAD default Training",
            title_right="Auxiliary\n GRAD-GPAD sex balanced Training",
        )

        # Additional experiments
        # calculate_lifelong_learning_apcer_generalization_protocols(output_path)

    print(f"Reproducible Research Results: {output_path}")
    end = time.time()
    print(f"Elapsed time: {end-start} s")
