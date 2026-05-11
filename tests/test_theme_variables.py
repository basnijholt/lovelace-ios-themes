import unittest
from pathlib import Path

import yaml


THEMES_FILE = Path(__file__).resolve().parents[1] / "themes" / "ios-themes.yaml"

EXPECTED_FORM_VARIABLES = {
    "ha-color-form-background": "rgba(0, 0, 0, 0)",
    "ha-color-form-background-hover": "rgba(255, 255, 255, 0.05)",
    "ha-color-form-background-disabled": "rgba(0, 0, 0, 0.1)",
}

EXPECTED_PRIMARY_PALETTE = {
    "ha-color-primary-05": "#1a0800",
    "ha-color-primary-10": "#331100",
    "ha-color-primary-20": "#663300",
    "ha-color-primary-30": "#994400",
    "ha-color-primary-40": "#ff9409",
    "ha-color-primary-50": "#ff9f09",
    "ha-color-primary-60": "#ffb333",
    "ha-color-primary-70": "#ffcc66",
    "ha-color-primary-80": "#ffe099",
    "ha-color-primary-90": "#fff0cc",
    "ha-color-primary-95": "#fff8e6",
}


class ThemeVariablesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with THEMES_FILE.open() as f:
            cls.themes = yaml.safe_load(f)

    def test_all_expected_theme_variants_are_generated(self):
        self.assertEqual(28, len(self.themes))

    def test_all_themes_define_home_assistant_2026_4_form_backgrounds(self):
        for theme_name, theme in self.themes.items():
            with self.subTest(theme=theme_name):
                for key, expected_value in EXPECTED_FORM_VARIABLES.items():
                    self.assertEqual(expected_value, theme.get(key))

    def test_all_themes_define_current_primary_palette_tokens(self):
        for theme_name, theme in self.themes.items():
            with self.subTest(theme=theme_name):
                for key, expected_value in EXPECTED_PRIMARY_PALETTE.items():
                    self.assertEqual(expected_value, theme.get(key))

    def test_theme_names_declare_matching_home_assistant_color_mode(self):
        for theme_name, theme in self.themes.items():
            expected_mode = "dark" if "-dark-mode-" in theme_name else "light"

            with self.subTest(theme=theme_name):
                self.assertEqual({expected_mode: {}}, theme.get("modes"))

    def test_light_themes_use_dark_default_state_icons(self):
        for theme_name, theme in self.themes.items():
            if "-light-mode-" not in theme_name:
                continue

            with self.subTest(theme=theme_name):
                self.assertEqual("#333333", theme.get("state-icon-color"))


if __name__ == "__main__":
    unittest.main()
