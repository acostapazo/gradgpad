def legend_without_duplicate_labels(ax):
    handles, labels = ax.get_legend_handles_labels()
    unique = [
        (h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]
    ]
    unique_values = [
        (h, l) for h, l in sorted(unique, key=lambda tup: tup[1]) if "EER" not in l
    ]
    unique_values_eer = [(h, l) for h, l in unique if "EER" in l]
    unique_sorted = unique_values + unique_values_eer

    ncol = len(unique_sorted)
    last_values = [
        (line, label)
        for line, label in unique_sorted
        if label == "Attacks" or label == "Working Points"
    ]
    first_values = [
        (line, label)
        for line, label in unique_sorted
        if label != "Attacks" and label != "Working Points"
    ]
    unique_sorted = first_values + last_values

    bbox_to_anchor = None
    ax.legend(
        *zip(*unique_sorted),
        loc="upper center",
        bbox_to_anchor=bbox_to_anchor,
        ncol=ncol
    )


COLORS = {
    "MALE": "b",
    "FEMALE": "g",
    "YOUNG": "g",
    "ADULT": "b",
    "SENIOR": "y",
    "ATTACKS": "r",
    "YELLOW": "y",
    "PINK": "pink",
    "BROWN": "brown",
}

MARKERS = {"ATTACKS": "v"}
