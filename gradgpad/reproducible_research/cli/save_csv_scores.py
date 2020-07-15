import csv
import os
from typing import Dict

from gradgpad.reproducible_research import (
    quality_rbf_scores_grandtest_type_I_test,
    quality_linear_scores_grandtest_type_I_test,
)


def save_csv_scores(output_path: str):
    print("Saving scores to csv...")

    approaches = {
        "Quality RBF": quality_rbf_scores_grandtest_type_I_test,
        "Quality Linear": quality_linear_scores_grandtest_type_I_test,
    }
    for approach, scores in approaches.items():
        folder = approach.lower().replace(" ", "_")

        demographic_scores = {
            "gender": scores.get_fair_gender_subset(),
            "age": scores.get_fair_age_subset(),
            "skin_tone": scores.get_fair_skin_tone_subset(),
        }

        for demographic, fair_scores in demographic_scores.items():
            csv_output_path = f"{output_path}/csv/{folder}/{demographic}"
            os.makedirs(csv_output_path, exist_ok=True)
            scores_to_csv(fair_scores, approach, csv_output_path)


def scores_to_csv(fair_scores: Dict, approach: str, output_path: str):
    for demographic_name, scores in fair_scores.items():
        csv_data = []
        for id, score in scores.items():
            csv_data.append(
                {
                    "Approach": approach,
                    "Demographic Label": demographic_name,
                    "Id": id,
                    "Score": score,
                }
            )

        csv_file = f"{output_path}/{demographic_name.lower()}.csv"

        try:
            with open(csv_file, "w", newline="") as csvfile:
                writer = csv.DictWriter(
                    csvfile, fieldnames=["Approach", "Demographic Label", "Id", "Score"]
                )
                writer.writeheader()
                for data in csv_data:
                    writer.writerow(data)
        except IOError:
            print("I/O error")
