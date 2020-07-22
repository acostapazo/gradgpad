import argparse
import zipfile
import os

from gradgpad.reproducible_research.cli.reproducible_research import (
    reproducible_research,
)


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

    args = parser.parse_args()

    if args.reproducible_research:
        reproducible_research(args.output_path)

        if args.zip_folder:
            last_folder = args.output_path.split("/")[-1]
            zipf = zipfile.ZipFile(f"{last_folder}.zip", "w", zipfile.ZIP_DEFLATED)
            zipdir(args.output_path, zipf)
            zipf.close()
