# Render themes, creates them as separate files and as
# one combined file `ios-themes.yaml`.
# Part of https://github.com/basnijholt/lovelace-ios-themes

from pathlib import Path

import jinja2
import yaml
from PIL import Image
from PIL import ImageColor

with open("settings-light-dark.yaml", "r") as f:
    all_settings = yaml.safe_load(f)


def parse(x):
    return x if "#" not in x else f'"{x}"'


def average_color(fname):
    color = Image.open(fname).resize((1, 1)).getpixel((0, 0))
    hex_color = "#{:02x}{:02x}{:02x}".format(*color)
    rgb_color = ImageColor.getrgb(hex_color)
    return "rgba({}, {}, {}, 0.8)".format(*rgb_color)


fname = "themes/ios-themes.yaml"

with open(fname, "w") as f:
    f.write("---\n# From https://github.com/basnijholt/lovelace-ios-themes")


for background in Path("themes").glob("homekit-bg-*.jpg"):
    color = background.stem.split("homekit-bg-")[-1]
    app_header_background_color = average_color(background)
    for which in ["light", "dark"]:
        for state_icon_yellow in [False, True]:
            settings = {k: parse(v[which]) for k, v in all_settings.items()}

            if state_icon_yellow:
                settings["state_icon_active_color"] = "rgba(255, 214, 10, 1)"
                suffix = "-alternative"
            else:
                suffix = ""

            with open("template.jinja2") as f:
                template = jinja2.Template("".join(f.readlines()))

            result = template.render(
                **settings,
                app_header_background_color=app_header_background_color,
                which=which,
                background_jpg=str(background.name),
                color=color,
                suffix=suffix,
            )

            with open(fname, "a") as f:
                f.write("\n" + result + "\n")
