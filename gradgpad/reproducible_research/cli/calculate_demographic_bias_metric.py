import json
import numpy as np
from statistics import mean


def find_nearest(array, value):
    idx, val = min(enumerate(array), key=lambda x: abs(x[1] - value))
    return idx


def calculate_demographic_bias_metric(
    demographic_percentiles,
    approaches,
    output_path_percentiles,
    calculate_sex=True,
    calculate_age=True,
    calculate_skin_tone=True,
    verbose_text: str = "> Demographic | Calculating Demographic Bias Metric (DBM)...",
):
    print(verbose_text)

    p = np.linspace(0, 100, 6001)

    bpcer_values = {}
    for demographic, approaches_percentiles in demographic_percentiles.items():

        bpcer_values[demographic] = {}
        for (
            approach,
            (percentiles, lower_frr_th_test, higher_frr_th_test),
        ) in approaches_percentiles.items():

            bpcer_values[demographic][approach] = {}

            for sub_demographic, x in percentiles.items():
                if sub_demographic == "ATTACKS":
                    continue
                y = 100 - p

                indexes = [
                    find_nearest(x, working_point)
                    for working_point in np.arange(
                        lower_frr_th_test, higher_frr_th_test, 0.001
                    )
                ]
                y_roi = y[indexes]
                bpcer_values[demographic][approach][sub_demographic] = y_roi

    def calculate_sex_bias(bpcer_values):
        sex_bias = {}
        for approach in approaches:
            male = bpcer_values["sex"][approach]["MALE"]
            female = bpcer_values["sex"][approach]["FEMALE"]
            sex_bias_metric = mean(abs(male - female))
            # print(f"Sex - {approach}: {sex_bias_metric}")
            sex_bias[f"Sex - {approach}"] = sex_bias_metric
        return sex_bias

    def calculate_age_bias(bpcer_values):
        age_bias = {}
        for approach in approaches:
            young = bpcer_values["age"][approach]["YOUNG"]
            adult = bpcer_values["age"][approach]["ADULT"]
            senior = bpcer_values["age"][approach]["SENIOR"]

            age_bias_metric = mean(
                [
                    mean(abs(young - adult)),
                    mean(abs(young - senior)),
                    mean(abs(senior - adult)),
                ]
            )
            # print(f"Age - {approach} - Y-A: {mean(abs(young - adult))}")
            # print(f"Age - {approach} - Y-S: {mean(abs(young - senior))}")
            # print(f"Age - {approach} - S-A: {mean(abs(senior - adult))}")
            # print(f"Age - {approach}: {age_bias_metric}")
            age_bias[f"Age - {approach}"] = age_bias_metric
        return age_bias

    def calculate_skin_tone_bias(bpcer_values):
        skin_tone_bias = {}
        for approach in approaches:
            yellow = bpcer_values["grouped_skin_tone"][approach]["YELLOW"]
            pink = bpcer_values["grouped_skin_tone"][approach]["PINK"]
            brown = bpcer_values["grouped_skin_tone"][approach]["BROWN"]

            skin_tone_bias_metric = mean(
                [
                    mean(abs(yellow - pink)),
                    mean(abs(yellow - brown)),
                    mean(abs(brown - pink)),
                ]
            )
            # print(f"Age - {approach} - Y-A: {mean(abs(yellow - pink))}")
            # print(f"Age - {approach} - Y-S: {mean(abs(yellow - brown))}")
            # print(f"Age - {approach} - S-A: {mean(abs(brown - pink))}")
            # print(f"Skin Tone - {approach}: {skin_tone_bias_metric}")
            skin_tone_bias[f"Skin Tone - {approach}"] = skin_tone_bias_metric
        return skin_tone_bias

    bias = {}
    if calculate_sex:
        sex_bias = calculate_sex_bias(bpcer_values)
        bias = {**bias, **sex_bias}
    if calculate_age:
        age_bias = calculate_age_bias(bpcer_values)
        bias = {**bias, **age_bias}
    if calculate_skin_tone:
        skin_tone_bias = calculate_skin_tone_bias(bpcer_values)
        bias = {**bias, **skin_tone_bias}

    filename = f"{output_path_percentiles}/demographic_metrics.json"
    with open(filename, "w") as fp:
        json.dump(bias, fp, indent=4)
