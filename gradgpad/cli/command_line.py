import argparse
import sys
import zipfile
import os

from gradgpad.foundations.metrics.metrics import Metrics
from gradgpad.reproducible_research.cli.reproducible_research import (
    reproducible_research,
)
from gradgpad.foundations.scores.subset import Subset


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--reproducible-research",
        "-rr",
        dest="reproducible_research",
        action="store_true",
        help="Create a folder with reproducible research results",
    )
    parser.add_argument(
        "--zip", "-z", dest="zip_folder", action="store_true", help="Zip result folder"
    )
    parser.add_argument("--output-path", "-o", dest="output_path", help="Output path")
    parser.add_argument(
        "--show-hist",
        "-sh",
        dest="show_hist",
        action="store_true",
        help="Show hist from score filename",
    )
    parser.add_argument(
        "--score-filename-devel",
        "-sfd",
        dest="score_filename_devel",
        help="Score filename Devel",
    )
    parser.add_argument(
        "--score-filename-test",
        "-sft",
        dest="score_filename_test",
        help="Score filename Tests",
    )
    parser.add_argument(
        "--show-path",
        "-sp",
        dest="show_path",
        action="store_true",
        help="Show Package Path",
    )
    parser.add_argument(
        "--show-scores-path",
        "-ssp",
        dest="show_scores_path",
        action="store_true",
        help="Show Scores Path",
    )

    args = parser.parse_args()

    if args.show_path:
        sys.stdout.write(os.getenv("GRADGPAD_PATH"))
        sys.exit(0)

    if args.show_scores_path:
        sys.stdout.write(os.getenv("GRADGPAD_SCORES_PATH"))
        sys.exit(0)

    if args.reproducible_research:
        reproducible_research(args.output_path)
        if args.zip_folder:
            last_folder = args.output_path.split("/")[-1]
            zip_filename = f"{last_folder}.zip"
            print(f"Zipping output folder -> {zip_filename}")
            zipf = zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED)
            zipdir(args.output_path, zipf)
            zipf.close()

    if args.show_hist:

        if not args.score_filename_devel and not args.score_filename_test:
            print(
                "Please add --score-filename-devel <path-to-your-filename> --score-filename-test <path-to-your-filename> to your command"
            )
            return

        try:
            from gradgpad.reproducible_research import Scores
            from gradgpad.tools.evaluation import save_histogram

            scores_devel = Scores.from_filename(args.score_filename_devel)
            scores_test = Scores.from_filename(args.score_filename_test)

            eer_threshold = Metrics(scores_devel, scores_test).get_eer_th(Subset.DEVEL)

            data = {
                "scores": scores_test.get_numpy_scores(),
                "labels": scores_test.get_numpy_labels(),
            }

            save_histogram(
                data,
                args.score_filename_test,
                genuine_label=0,
                normalize_hist=False,
                th=eer_threshold,
                th_legend="EER @ Devel",
                only_show=True,
            )
        except Exception as error:
            print(
                "Please add a valid filename --score-filename-devel <path-to-your-filename> --score-filename-test <path-to-your-filename> to your command"
            )
            print(str(error))
