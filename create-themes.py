# Render themes, creates them as separate files and as
# one combined file `ios-themes.yaml`.
# Part of https://github.com/basnijholt/lovelace-ios-themes

import base64
from pathlib import Path

import jinja2
import yaml

with open("settings-light-dark.yaml", "r") as f:
    all_settings = yaml.safe_load(f)


def parse(x):
    return x if "#" not in x else f'"{x}"'


with open(f"ios-themes.yaml", "w") as f:
    f.write("---\n# From https://github.com/basnijholt/lovelace-ios-themes")


for background in Path("backgrounds").glob("homekit-bg-*.jpg"):
    color = background.stem.split("homekit-bg-")[-1]
    for which in ["light", "dark"]:
        settings = {k: parse(v[which]) for k, v in all_settings.items()}

        with open("template.jinja2") as f:
            template = jinja2.Template("".join(f.readlines()))

        with background.open("rb") as f:
            background_base64 = base64.b64encode(f.read()).decode()

        result = template.render(
            **settings, which=which, background_base64=background_base64, color=color
        )
        with open(f"themes/ios-{which}-mode-{color}.yaml", "w") as f:
            f.write("---\n" + result + "\n")

        with open(f"ios-themes.yaml", "a") as f:
            f.write("\n" + result + "\n")
