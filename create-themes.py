# Render themes, creates them as separate files and as
# one combined file `ios-themes.yaml`.
# Part of https://github.com/basnijholt/lovelace-ios-themes

from pathlib import Path

import jinja2
import yaml
from PIL import Image, ImageColor

with open("settings-light-dark.yaml") as f:
    all_settings = yaml.safe_load(f)

COMMIT = "a37376d918fcfe4785be99910dc9a7200ac37da9"

BASE_URL = (
    f"https://cdn.jsdelivr.net/gh/basnijholt/lovelace-ios-themes@{COMMIT}/themes"
)


def parse(x):
    return x if "#" not in x else f'"{x}"'


def average_color(fname):
    color = Image.open(fname).resize((1, 1)).getpixel((0, 0))
    hex_color = "#{:02x}{:02x}{:02x}".format(*color)
    rgb_color = ImageColor.getrgb(hex_color)
    return "rgba({}, {}, {}, 0.4)".format(*rgb_color)


def fname_to_url(background: Path) -> str:
    return f"{BASE_URL}/{background.name}"


def fname_to_local_path(background: Path) -> str:
    return f"/local/ios-themes/{background.name}"


BACKGROUND_COLORS = {
    # Suggested by @okets in issue #42
    "blue-red": "rgba(30, 2, 61, 0.4)",
    "dark-blue": "rgba(48, 69, 124, 0.4)",
    "dark-green": "rgba(48, 89, 71, 0.4)",
    "light-blue": "rgba(1, 195, 220, 0.4)",
    "light-green": "rgba(114, 188, 139, 0.4)",
    "orange": "rgba(255, 229, 116, 0.4)",
    "red": "rgba(234, 88, 63, 0.4)",
}

fname = Path("themes/ios-themes.yaml")
fname.parent.mkdir(parents=True, exist_ok=True)

with fname.open("w") as f:
    f.write("---\n# From https://github.com/basnijholt/lovelace-ios-themes")
for background in sorted(Path("themes").glob("homekit-bg-*.jpg")):
    color = background.stem.split("homekit-bg-")[-1]
    if color in BACKGROUND_COLORS:
        app_header_background_color = BACKGROUND_COLORS[color]
    else:
        app_header_background_color = average_color(background)
    for which in ["light", "dark"]:
        for standard in [False, True]:
            settings = {k: parse(v[which]) for k, v in all_settings.items()}

            if standard:
                settings["state_icon_active_color"] = "rgba(255, 214, 10, 1)"
                suffix = ""
            else:
                suffix = "-alternative"

            with open("template.jinja2") as f:
                template = jinja2.Template("".join(f.readlines()))

            result = template.render(
                **settings,
                which=which,
                app_header_background_color=app_header_background_color,
                background=fname_to_url(background)
                if standard
                else fname_to_local_path(background),
                color=color,
                suffix=suffix,
            )

            with fname.open("a") as f:
                f.write("\n" + result + "\n")
