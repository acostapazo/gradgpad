import os

from gradgpad.annotations.spai import SpaiColor
from gradgpad.evaluation.metrics.metrics import Metrics
from gradgpad.evaluation.plots.det_curve import det_curve
from gradgpad.evaluation.plots.histogram import save_histogram
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.reproducible_research.scores.scores_provider import ScoresProvider
from gradgpad.reproducible_research.scores.subset import Subset


def calculate_hists_and_curves(output_path: str):
    print("Calculating Hists and Curves...")

    output_path_hists_and_curves = f"{output_path}/hists_and_curves"
    os.makedirs(output_path_hists_and_curves, exist_ok=True)

    approach_protocols_subset_scores = {
        "Quality SVM RBF": ScoresProvider.all(Approach.QUALITY_RBF),
        # "Quality SVM LINEAR": ScoresProvider.all(Approach.QUALITY_LINEAR),
        "Auxiliary": ScoresProvider.all(Approach.AUXILIARY),
    }
    for approach, protocols_subset_scores in approach_protocols_subset_scores.items():

        protocol_metrics = {}
        for protocol_name, subset_scores in protocols_subset_scores.items():
            if protocol_name != Protocol.GRANDTEST.value:
                continue
            protocol_metrics[protocol_name] = Metrics(
                devel_scores=subset_scores.get("devel"),
                test_scores=subset_scores.get("test"),
            )

        for protocol_name, subset_scores in protocols_subset_scores.items():
            if protocol_name != Protocol.GRANDTEST.value:
                continue
            approach_name = approach.replace(" ", "_").lower()
            output_path_hists_and_curves = (
                f"{output_path}/hists_and_curves/{approach_name}/{protocol_name}"
            )
            os.makedirs(output_path_hists_and_curves, exist_ok=True)

            metrics = protocol_metrics.get(protocol_name)
            eer_th = metrics.get_eer_th(Subset.DEVEL)

            for subset, scores in subset_scores.items():

                data = {
                    "scores": scores.get_numpy_scores(),
                    "labels": scores.get_numpy_labels(),
                }

                output_det_filename = f"{output_path_hists_and_curves}/{subset}_det.png"
                det_curve(data, output_det_filename)

                for normalize_hist in [True, False]:
                    if normalize_hist:
                        output_hist_filename = (
                            f"{output_path_hists_and_curves}/{subset}_hist_norm.png"
                        )
                    else:
                        output_hist_filename = (
                            f"{output_path_hists_and_curves}/{subset}_hist.png"
                        )
                    save_histogram(
                        data,
                        output_hist_filename,
                        genuine_label=0,
                        th=eer_th,
                        th_legend="EER @ Devel",
                        normalize_hist=normalize_hist,
                    )

                if protocol_name == Protocol.GRANDTEST.value:
                    calculate_hists_and_curves_pai_types(
                        output_path_hists_and_curves, subset, scores, eer_th
                    )


def calculate_hists_and_curves_pai_types(
    output_path_hists_and_curves, subset, scores, eer_th
):
    output_det_filename = f"{output_path_hists_and_curves}/{subset}_det_detail.png"

    data = {
        "scores": scores.get_numpy_scores(),
        "labels": scores.get_numpy_labels_by_type_pai(),
    }

    det_curve(
        data,
        output_det_filename,
        subtypes={1: "PAI Type I", 2: "PAI Type II", 3: "PAI Type III", 0: "All"},
        colors={
            1: SpaiColor.PAI_TYPE_I.value,
            2: SpaiColor.PAI_TYPE_II.value,
            3: SpaiColor.PAI_TYPE_III.value,
            0: "b",
        },
    )

    for normalize_hist in [True, False]:
        if normalize_hist:
            output_hist_filename = (
                f"{output_path_hists_and_curves}/{subset}_hist_norm_detail.png"
            )
        else:
            output_hist_filename = (
                f"{output_path_hists_and_curves}/{subset}_hist_detail.png"
            )

        save_histogram(
            data,
            output_hist_filename,
            genuine_label=0,
            th=eer_th,
            th_legend="EER @ Devel",
            normalize_hist=normalize_hist,
            subtypes=["PAI Type I", "PAI Type II", "PAI Type III"],
        )
