import numpy as np


VALUE_NOT_VALID_WORKING_POINT = 1.0
THRESHOLD_NOT_VALID_WORKING_POINT = -1.0
NOT_VALID_WORKING_POINT = (
    VALUE_NOT_VALID_WORKING_POINT,
    VALUE_NOT_VALID_WORKING_POINT,
    THRESHOLD_NOT_VALID_WORKING_POINT,
)


def get_target_value_fixing_working_point(
    fixed_working_point, targeted_values, fixing_values, thresholds, interpolated=False
):
    if not isinstance(targeted_values, np.ndarray):
        targeted_values = np.array(targeted_values)
    if not isinstance(fixing_values, np.ndarray):
        fixing_values = np.array(fixing_values)
    if not isinstance(thresholds, np.ndarray):
        thresholds = np.array(thresholds)

    if (targeted_values == fixing_values).all():
        return NOT_VALID_WORKING_POINT

    lower_near_idx = np.abs(targeted_values - fixed_working_point).argmin()

    if (
        not interpolated
        or lower_near_idx == 0
        and targeted_values[lower_near_idx] > fixed_working_point
    ):
        return (
            targeted_values[lower_near_idx],
            fixing_values[lower_near_idx],
            thresholds[lower_near_idx],
        )
    else:
        upper_near_idx = lower_near_idx
        if lower_near_idx == len(targeted_values) - 1 or lower_near_idx == 0:
            upper_near_idx == lower_near_idx
        elif targeted_values[lower_near_idx] < fixed_working_point:
            if targeted_values[lower_near_idx + 1] >= targeted_values[lower_near_idx]:
                upper_near_idx = lower_near_idx + 1
            else:
                upper_near_idx = lower_near_idx - 1
        else:
            if targeted_values[lower_near_idx + 1] <= targeted_values[lower_near_idx]:
                upper_near_idx = lower_near_idx + 1
            else:
                upper_near_idx = lower_near_idx - 1

        if (
            lower_near_idx > upper_near_idx
        ):  # targeted_values[lower_near_idx] >= fixed_working_point >= targeted_values[upper_near_idx]:
            l_idx = lower_near_idx
            lower_near_idx = upper_near_idx
            upper_near_idx = l_idx

        # if targeted_values[near_idx] <= fixed_working_point <= targeted_values[near_idx - 1]:
        # if targeted_values[near_idx] <= fixed_working_point:
        # if targeted_values[near_idx] >= fixed_working_point:
        #     lower_idx = near_idx - 1
        # else:
        #     lower_idx = near_idx
        #     near_idx = near_idx + 1

        # if near_idx > 99: # targeted_values.size - 1
        #     near_idx = near_idx - 1
        #     lower_idx = lower_idx - 1

        x0 = targeted_values[lower_near_idx]
        x1 = targeted_values[upper_near_idx]

        y0 = fixing_values[lower_near_idx]
        y1 = fixing_values[upper_near_idx]
        t0 = thresholds[lower_near_idx]
        t1 = thresholds[upper_near_idx]

        if t0 == t1 == 1.0:
            return NOT_VALID_WORKING_POINT

        if x1 - x0 == 0.0:
            m = 0
            mt = 0
        else:
            m = (y1 - y0) / (x1 - x0)
            mt = (t1 - t0) / (x1 - x0)

        target_val = fixed_working_point
        fixed_val = (target_val - x0) * m + y0
        threshold_val = (target_val - x0) * mt + t0

        return target_val, fixed_val, threshold_val
