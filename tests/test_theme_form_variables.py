import unittest
from pathlib import Path

import yaml


THEMES_FILE = Path(__file__).resolve().parents[1] / "themes" / "ios-themes.yaml"

EXPECTED_FORM_VARIABLES = {
    "ha-color-form-background": "rgba(0, 0, 0, 0)",
    "ha-color-form-background-hover": "rgba(255, 255, 255, 0.05)",
    "ha-color-form-background-disabled": "rgba(0, 0, 0, 0.1)",
}


class ThemeFormVariablesTest(unittest.TestCase):
    def test_all_themes_define_home_assistant_2026_4_form_backgrounds(self):
        with THEMES_FILE.open() as f:
            themes = yaml.safe_load(f)

        self.assertEqual(28, len(themes))

        for theme_name, theme in themes.items():
            with self.subTest(theme=theme_name):
                for key, expected_value in EXPECTED_FORM_VARIABLES.items():
                    self.assertEqual(expected_value, theme.get(key))


if __name__ == "__main__":
    unittest.main()
