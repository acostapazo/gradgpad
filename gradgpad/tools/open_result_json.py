import json
import traceback


def open_result_json(filename, verbose=False):
    try:
        with open(filename, "r") as f:
            results: dict = json.load(f)
        if verbose:
            print(f"Loaded result for {len(results.keys())} protocols from {filename}")
    except:  # noqa E722
        traceback.print_exc()
        print(f"Not loaded anything from {filename}")
        results = {}
    return results
