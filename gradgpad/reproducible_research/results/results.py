import os

from gradgpad.tools.open_result_json import open_result_json

REPRODUCIBLE_RESEARCH_RESULTS_DIR = os.path.abspath(os.path.dirname(__file__))


quality_results = open_result_json(
    f"{REPRODUCIBLE_RESEARCH_RESULTS_DIR}/quality_results.json"
)
quality_linear_results = open_result_json(
    f"{REPRODUCIBLE_RESEARCH_RESULTS_DIR}/quality_linear_results.json"
)
auxiliary_results = open_result_json(
    f"{REPRODUCIBLE_RESEARCH_RESULTS_DIR}/auxiliary_results.json"
)

# Cross-Dataset
quality_results_cross_dataset = {
    k: v for k, v in quality_results.items() if "Cross-Dataset" in k
}
quality_linear_results_cross_dataset = {
    k: v for k, v in quality_linear_results.items() if "Cross-Dataset" in k
}
auxiliary_results_cross_dataset = {
    k: v for k, v in auxiliary_results.items() if "Cross-Dataset" in k
}


# LODO
quality_results_lodo = {k: v for k, v in quality_results.items() if "LODO" in k}
quality_linear_results_lodo = {
    k: v for k, v in quality_linear_results.items() if "LODO" in k
}
auxiliary_results_lodo = {k: v for k, v in auxiliary_results.items() if "LODO" in k}


# Cross-Device
quality_results_cross_device = {
    k: v for k, v in quality_results.items() if "Cross-Device" in k
}
quality_linear_results_cross_device = {
    k: v for k, v in quality_linear_results.items() if "Cross-Device" in k
}
auxiliary_results_cross_device = {
    k: v for k, v in auxiliary_results.items() if "Cross-Device" in k
}

# Unseen-Attack
quality_results_unseen_attack = {
    k: v for k, v in quality_results.items() if "Unseen-Attack" in k
}
quality_linear_results_unseen_attack = {
    k: v for k, v in quality_linear_results.items() if "Unseen-Attack" in k
}
# auxiliary_results_unseen_attack = {
#     k: v for k, v in auxiliary_results.items() if "Unseen-Attack" in k
# }

# Demographics
quality_results_gender = {k: v for k, v in quality_results.items() if "Gender" in k}
quality_linear_results_gender = {
    k: v for k, v in quality_linear_results.items() if "Gender" in k
}
auxiliary_results_gender = {k: v for k, v in auxiliary_results.items() if "Gender" in k}


quality_results_skin_tone = {
    k: v for k, v in quality_results.items() if "Skin Tone" in k
}
quality_linear_results_skin_tone = {
    k: v for k, v in quality_linear_results.items() if "Skin Tone" in k
}
auxiliary_results_skin_tone = {
    k: v for k, v in auxiliary_results.items() if "Skin Tone" in k
}

quality_results_age = {k: v for k, v in quality_results.items() if "Age" in k}
quality_linear_results_age = {
    k: v for k, v in quality_linear_results.items() if "Age" in k
}
auxiliary_results_age = {k: v for k, v in auxiliary_results.items() if "Age" in k}
