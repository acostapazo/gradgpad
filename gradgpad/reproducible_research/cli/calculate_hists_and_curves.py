import os

from gradgpad.evaluation.plots.det_curve import det_curve
from gradgpad.evaluation.plots.histogram import save_histogram
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.scores_provider import ScoresProvider


def calculate_hists_and_curves(output_path: str):
    print("Calculating Hists and Curves...")

    output_path_hists_and_curves = f"{output_path}/hists_and_curves"
    os.makedirs(output_path_hists_and_curves, exist_ok=True)

    approach_protocols_subset_scores = {
        "Quality SVM RBF": ScoresProvider.all(Approach.QUALITY_RBF),
        "Quality SVM LINEAR": ScoresProvider.all(Approach.QUALITY_LINEAR),
        "Auxiliary": ScoresProvider.all(Approach.AUXILIARY),
    }
    for approach, protocols_subset_scores in approach_protocols_subset_scores.items():

        for protocol_name, subset_scores in protocols_subset_scores.items():

            approach_name = approach.replace(" ", "_").lower()
            output_path_hists_and_curves = (
                f"{output_path}/hists_and_curves/{approach_name}/{protocol_name}"
            )
            os.makedirs(output_path_hists_and_curves, exist_ok=True)

            for subset, scores in subset_scores.items():

                output_det_filename = f"{output_path_hists_and_curves}/{subset}_det.png"
                output_hist_filename = (
                    f"{output_path_hists_and_curves}/{subset}_hist.png"
                )

                data = {
                    "scores": scores.get_numpy_scores(),
                    "labels": scores.get_numpy_labels(),
                }
                det_curve(data, output_det_filename)
                save_histogram(data, output_hist_filename, genuine_label=0)
