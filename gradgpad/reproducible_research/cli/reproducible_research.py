import os

from gradgpad.reproducible_research.cli.calculate_apcer_by_pai import (
    calculate_apcer_by_pai,
)
from gradgpad.reproducible_research.cli.save_csv_scores import save_csv_scores


def reproducible_research(output_path: str):
    os.makedirs(output_path, exist_ok=True)
    calculate_apcer_by_pai(output_path)

    save_csv_scores(output_path)

    print(f"Reproducible Research Results: {output_path}")
