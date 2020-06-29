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
}


def get_fancy_protocol(original_protocol_name):
    fancy_protocol_name = fancy_protocol_correspondences.get(original_protocol_name)
    return fancy_protocol_name if fancy_protocol_name else original_protocol_name
