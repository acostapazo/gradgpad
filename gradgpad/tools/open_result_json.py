import json
import traceback

from gradgpad.tools.fancy_protocol_correspondences import get_fancy_protocol


def open_result_json(filename, apply_fancy_names=True, verbose=False):
    try:
        with open(filename, "r") as f:
            results: dict = json.load(f)
            if apply_fancy_names:
                results = {get_fancy_protocol(k): v for k, v in results.items()}

        if verbose:
            print(f"Loaded result for {len(results.keys())} protocols from {filename}")
    except:  # noqa E722
        traceback.print_exc()
        print(f"Not loaded anything from {filename}")
        results = {}
    return results
