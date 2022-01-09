from typing import List

from gradgpad.foundations.annotations.correspondences import ANNOTATION_CORRESPONDENCES


def calculate_pai_stats(annotated_samples: List):
    pai_stats = {
        "num_genuines": 0,
        "num_attacks": 0,
        "num_samples_pas_type": {"pas_type_1": 0, "pas_type_2": 0, "pas_type_3": 0},
        "num_coarse_grained_pai": {
            "print": 0,
            "replay": 0,
            "mask": 0,
            "makeup": 0,
            "partial": 0,
        },
        "num_fine_grained_pai": {
            "print low quality": 0,
            "print medium quality": 0,
            "print high quality": 0,
            "replay low quality": 0,
            "replay medium quality": 0,
            "replay high quality": 0,
            "mask paper": 0,
            "mask rigid": 0,
            "mask silicone": 0,
            "makeup cosmetic": 0,
            "makeup impersonation": 0,
            "makeup obfuscation": 0,
            "partial funny eyes": 0,
            "partial periocular": 0,
            "partial paper glasses": 0,
            "partial upper half": 0,
            "partial lower half": 0,
        },
    }

    for annotation in annotated_samples:
        categorization = annotation.categorization
        coarse_grain_pai = ANNOTATION_CORRESPONDENCES["categorization"][
            "coarse_grained_pai"
        ][categorization.get("coarse_grained_pai")]
        fine_grain_pai = ANNOTATION_CORRESPONDENCES["categorization"][
            "fine_grained_pai"
        ][categorization.get("fine_grained_pai")]

        if coarse_grain_pai == "genuine":
            pai_stats["num_genuines"] += 1
        else:
            pai_stats["num_attacks"] += 1
            pai_stats["num_coarse_grained_pai"][coarse_grain_pai] += 1
            pai_stats["num_fine_grained_pai"][fine_grain_pai] += 1
            pas_type = categorization["pas_type"]
            pai_stats["num_samples_pas_type"][f"pas_type_{pas_type}"] += 1

    pai_stats = add_percentages_to_pai_stats(pai_stats, "num_samples_pas_type")
    pai_stats = add_percentages_to_pai_stats(pai_stats, "num_coarse_grained_pai")
    pai_stats = add_percentages_to_pai_stats(pai_stats, "num_fine_grained_pai")
    return pai_stats


def add_percentages_to_pai_stats(pai_stats: dict, key_stat: str) -> dict:

    total_values = sum(pai_stats.get(key_stat).values())
    stats = pai_stats.get(key_stat)

    pai_stats[f"percentage_{key_stat}"] = {}
    for k, v in stats.items():
        pai_stats[f"percentage_{key_stat}"][k] = v / total_values * 100

    return pai_stats
