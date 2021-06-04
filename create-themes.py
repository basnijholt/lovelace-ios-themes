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
    return "rgba({}, {}, {}, 0.4)".format(*rgb_color)


folder_fname = [
    ("hacsfiles", Path("themes/ios-themes.yaml")),
    ("local", Path("manual-install/ios-themes.yaml")),
]
for folder, fname in folder_fname:
    fname.parent.mkdir(parents=True, exist_ok=True)
    with fname.open("w") as f:
        f.write("---\n# From https://github.com/basnijholt/lovelace-ios-themes")
    for background in Path("themes").glob("homekit-bg-*.jpg"):
        color = background.stem.split("homekit-bg-")[-1]
        app_header_background_color = average_color(background)

        for state_icon_yellow in [False, True]:
            settings = {
                k: {_k: parse(_v) for _k, _v in v.items()}
                for k, v in all_settings.items()
            }
            if state_icon_yellow:
                dct = settings["state_icon_active_color"]
                dct["light"] = dct["dark"] = "rgba(255, 214, 10, 1)"
                suffix = ""
            else:
                suffix = "-alternative"

            with open("template.jinja2") as f:
                template = jinja2.Template("".join(f.readlines()))

            result = template.render(
                **settings,
                folder=folder,
                app_header_background_color=app_header_background_color,
                background_jpg=str(background.name),
                color=color,
                suffix=suffix,
            )

            with fname.open("a") as f:
                f.write("\n" + result + "\n")
