ANNOTATION_CORRESPONDENCES = {
    "categorization": {
        "coarse_grained_pai": {
            0: "genuine",
            1: "print",
            2: "replay",
            3: "mask",
            5: "makeup",
            6: "partial",
        },
        "fine_grained_pai": {
            0: "genuine",
            1: "print low quality",  # dpi <= 600
            2: "print medium quality",  # 609 < dpi <= 1000
            3: "print high quality",  # dpi > 1000
            4: "replay low quality",  # res <= 480p
            5: "replay medium quality",  # 480p < res < 1080p
            6: "replay high quality",  # res >= 1080p
            7: "mask paper",  # paper masks
            8: "mask rigid",  # non-flexible plaster-like
            9: "mask silicone",  # silicone mask
            10: "makeup cosmetic",  # professional makeup (look older)
            11: "makeup impersonation",  # makeup to look like another person
            12: "makeup obfuscation",  # try to hide your identity
            13: "partial funny eyes",  # small occlusions of the face like party glasses
            14: "partial periocular",
            # occlusions that attempts to replace some parts of the face (periocular region)
            15: "partial paper glasses",  # minor occlusions like paper glasses,
            16: "partial upper half",  # occlusions that replaces larger areas of the face (upper half)
            17: "partial lower half",  # occlusions that replaces larger areas of the face (lower half)
        },
    },
    "attributes": {
        "person": {
            "sex": {0: "male", 1: "female"},
            "skin_tone": {
                1: "light pink",
                2: "light yellow",
                3: "medium pink brown",
                4: "medium yellow brown",
                5: "medium dark brown",
                6: "dark brown",
            },
            "age": {0: "young", 1: "adult", 2: "senior"},
        },
        "conditions": {
            "lighting": {0: "controlled", 1: "adverse", 2: "no_info"},
            "capture_device": {
                -1: "no_info",
                0: "webcam low quality",  # SD res
                1: "webcam high quality",  # HD res
                2: "mobile/tablet low quality",  # SD res
                3: "mobile/tablet high quality",  # HD res
                4: "digital camera low quality",  # SD res
                5: "digital camera high quality",  # HD res
            },
        },
    },
}
