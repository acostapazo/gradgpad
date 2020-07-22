import os

from gradgpad.reproducible_research.cli.calculate_apcer_generalization_protocols import (
    calculate_apcer_generalization_protocols,
)
from gradgpad.reproducible_research.cli.calculate_demographic_bpcer_bar_chart import (
    calculate_demographic_bpcer_bar_chart,
)
from gradgpad.reproducible_research.cli.calculate_hists_and_curves import (
    calculate_hists_and_curves,
)
from gradgpad.reproducible_research.cli.save_csv_scores import save_csv_scores
from gradgpad.reproducible_research.cli.calculate_apcer_by_pai import (
    calculate_apcer_by_pai,
)
from gradgpad.reproducible_research.cli.summary_table import summary_table


def reproducible_research(output_path: str):
    os.makedirs(output_path, exist_ok=True)
    summary_table(output_path)
    calculate_hists_and_curves(output_path)
    calculate_apcer_by_pai(output_path)
    calculate_apcer_generalization_protocols(output_path)
    calculate_demographic_bpcer_bar_chart(output_path)
    save_csv_scores(output_path)

    print(f"Reproducible Research Results: {output_path}")
