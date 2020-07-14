import argparse

from gradgpad.reproducible_research.cli.reproducible_research import (
    reproducible_research,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--reproducible-research",
        "-rr",
        dest="reproducible_research",
        action="store_true",
        help="Create a folder with reproducible research results",
    )
    parser.add_argument("--output-path", "-o", dest="output_path", help="Output path")

    args = parser.parse_args()

    if args.reproducible_research:
        reproducible_research(args.output_path)
