fancy_protocol_correspondences = {
    "age-bias-grad-gpad-young": "Age - Young",
    "age-bias-grad-gpad-adult": "Age - Adult",
    "age-bias-grad-gpad-senior": "Age - Senior",
    "gender-bias-grad-gpad-male": "Gender - Male",
    "gender-bias-grad-gpad-female": "Gender - Female",
    "skin-tone-bias-grad-gpad-light-pink": "Skin Tone - Light Pink",
    "skin-tone-bias-grad-gpad-light-yellow": "Skin Tone - Light Yellow",
    "skin-tone-bias-grad-gpad-medium-pink-brown": "Skin Tone - Medium Pink Brown",
    "skin-tone-bias-grad-gpad-medium-yellow-brown": "Skin Tone - Medium Yellow Brown",
    "skin-tone-bias-grad-gpad-medium-dark-brown": "Skin Tone - Medium Dark Brown",
    "skin-tone-bias-grad-gpad-dark-brown": "Skin Tone - Dark Brown",
    "cross-dataset-test-casia-fasd": "Cross-Dataset - CASIA-FASD",
    "cross-dataset-test-csmad": "Cross-Dataset - CSMAD",
    "cross-dataset-test-hkbu": "Cross-Dataset - HKBU",
    "cross-dataset-test-msu-mfsd": "Cross-Dataset - MSU-MFSD",
    "cross-dataset-test-oulu-npu": "Cross-Dataset - Oulu-NPU",
    "cross-dataset-test-replay-attack": "Cross-Dataset - Replay-Attack",
    "cross-dataset-test-replay-mobile": "Cross-Dataset - Replay-Mobile",
    "cross-dataset-test-rose-youtu": "Cross-Dataset - Rose-Youtu",
    "cross-dataset-test-siw": "Cross-Dataset - SiW",
    "cross-dataset-test-threedmad": "Cross-Dataset - 3DMAD",
    "cross-dataset-test-uvad": "Cross-Dataset - UVAD",
    "cross-dataset-test-siw-m": "Cross-Dataset - SiW-M",
    "cross-dataset-test-hkbuv2": "Cross-Dataset - HKBU v2",
    "cross-device-test-webcam": "Cross-Device - Webcam",
    "cross-device-test-mobile-tablet": "Cross-Device - Mobile|Tablet",
    "cross-device-test-digital_camera": "Cross-Device - Digital Camera",
    "unseen-attack-print": "Unseen-Attack - Print",
    "unseen-attack-replay": "Unseen-Attack - Replay",
    "unseen-attack-mask": "Unseen-Attack - Mask",
    "unseen-attack-makeup": "Unseen-Attack - Makeup",
    "unseen-attack-partial": "Unseen-Attack - Partial",
    "casia-fasd-leave-other-datasets-out": "LODO - CASIA-FASD",
    "csmad-leave-other-datasets-out": "LODO - CSMAD",
    "hkbu-leave-other-datasets-out": "LODO - HKBU",
    "msu-mfsd-leave-other-datasets-out": "LODO - MSU-MFSD",
    "oulu-npu-leave-other-datasets-out": "LODO - Oulu-NPU",
    "replay-attack-leave-other-datasets-out": "LODO - Replay-Attack",
    "replay-mobile-leave-other-datasets-out": "LODO - Replay-Mobile",
    "rose-youtu-leave-other-datasets-out": "LODO - Rose-Youtu",
    "siw-leave-other-datasets-out": "LODO - SiW",
    "threedmad-leave-other-datasets-out": "LODO - 3DMAD",
    "uvad-leave-other-datasets-out": "LODO - UVAD",
    "siw-m-leave-other-datasets-out": "LODO - SiW-M",
    "hkbuv2-leave-other-datasets-out": "LODO - HKBU v2",
}


def get_fancy_protocol(original_protocol_name):
    fancy_protocol_name = fancy_protocol_correspondences.get(original_protocol_name)
    return fancy_protocol_name if fancy_protocol_name else original_protocol_name
