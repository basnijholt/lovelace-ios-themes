# render template
import jinja2
import yaml
import base64


with open("light-dark.yaml", "r") as f:
    all_settings = yaml.safe_load(f)


def parse(x):
    return x if "#" not in x else f'"{x}"'


for bg in ["blue", "green", "blue-red", "dark-orange"]:
    for which in ["light", "dark"]:
        settings = {k: parse(v[which]) for k, v in all_settings.items()}

        with open("template.jijnja2.yaml") as f:
            temp = "".join(f.readlines())

        t = jinja2.Template(temp)

        with open(f"backgrounds/homekit-bg-{bg}.jpeg", "rb") as f:
            background_base64 = base64.b64encode(f.read()).decode()

        result = t.render(**settings, which=which, background_base64=background_base64)
        with open(f"themes/ios-{which}-mode-{bg}.yaml", "w") as f:
            f.write(result + "\n")
