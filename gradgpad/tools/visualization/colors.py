from random import randint

COLORS_LABEL_CORRESPONDENCES = {
    -1: "red",
    0: "green",
    1: "blue",
    2: "orange",
    3: "magenta",
    4: "indigo",
    5: "yellowgreen",
    6: "hotpink",
    7: "springgreen",
    8: "turquoise",
    9: "limegreen",
    10: "slategray",
    11: "rosybrown",
    12: "peru",
    13: "darkseagreen",
}


def get_color_random_style():
    colors = [
        "blue",
        "green",
        "red",
        "cyan",
        "magenta",
        "black",
        "brown",
        "chocolate",
        "fuchsia",
        "yellowgreen",
        "darkorange",
        "peru",
        "firebrick",
        "darkcyan",
        "lime",
        "gold",
        "olive",
        "royalblue",
        "teal",
        "violet",
        "darkviolet",
        "salmon",
        "bisque",
        "tan",
        "grey",
    ]
    linestyles = ["solid", "dotted", "dashed", "dashdot"]
    markers = [".", ",", "o", "v"]

    color_index = randint(0, len(colors) - 1)
    linestyle_index = randint(0, len(linestyles) - 1)
    markers_index = randint(0, len(markers) - 1)

    return colors[color_index], linestyles[linestyle_index], markers[markers_index]
