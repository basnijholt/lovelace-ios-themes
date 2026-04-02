# iOS Themes

[![Action Status](https://github.com/basnijholt/lovelace-ios-themes/workflows/yamllint/badge.svg)](https://github.com/basnijholt/lovelace-ios-themes/actions)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)
[![homeassistant_community](https://img.shields.io/badge/HA%20community-forum-brightgreen)](https://community.home-assistant.io/t/ios-dark-and-light-mode-with-easy-background-change/206215)
[![Github Stars](https://img.shields.io/github/stars/basnijholt/lovelace-ios-themes)](https://github.com/basnijholt/lovelace-ios-themes)

> The iOS Theme by @basnijholt and modified from @kalkih's [Gist](https://gist.github.com/kalkih/fbe84b371ef7f992c3bd51b235e2c299)

A generalized version of [*iOS Dark Mode Theme*](https://github.com/basnijholt/lovelace-ios-dark-mode-theme)!
This includes both **Dark and Light Mode** and 7 different HomeKit backgrounds.
Installing this theme adds 28 different themes:
- `ios-light-mode-dark-green`
- `ios-dark-mode-dark-green`
- `ios-light-mode-light-blue`
- `ios-dark-mode-light-blue`
- `ios-light-mode-light-green`
- `ios-dark-mode-light-green`
- `ios-light-mode-orange`
- `ios-dark-mode-orange`
- `ios-light-mode-blue-red`
- `ios-dark-mode-blue-red`
- `ios-light-mode-red`
- `ios-dark-mode-red`
- `ios-light-mode-dark-blue`
- `ios-dark-mode-dark-blue`
- `...` and versions with the `-alternative` suffix

## Screenshots

Screenshots of [my](https://github.com/basnijholt) Home-Assistant instance, [see the config files here :octocat:](https://github.com/basnijholt/home-assistant-config/).

Low quality `gif`, click [here](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/overview.mp4) to see a `mp4` (or scroll down).

[![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/overview.gif)](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/overview.mp4)

### Overview

![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/blue-red-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/blue-red-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/dark-blue-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/dark-blue-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/dark-green-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/dark-green-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/light-blue-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/light-blue-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/light-green-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/light-green-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/orange-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/orange-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/red-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/red-light.png)


## Installation

1. Install the theme via HACS.

* If you do not have HACS yet, [download and set it up](https://www.hacs.xyz/docs/use/download/download/) first — a GitHub account is required.
* In Home Assistant, open **HACS** from the sidebar.
* Search for `iOS Themes` and select it.
* In the bottom-right corner, select **Download**.

2. Add the following to your `configuration.yaml` (reboot required).

```yaml
frontend:
  ... # your configuration.
  themes: !include_dir_merge_named themes
  ... # your configuration.
```

3. Set the background on your dashboard.

Open your dashboard, select **Edit dashboard** (pencil icon) → **⋮ Open dashboard menu** → **Raw configuration editor**, and add this at the top level:

```yaml
background: var(--background-image)
```

So the end result will be something like [this example](https://github.com/basnijholt/home-assistant-config/blob/master/lovelace-ui.yaml).

## Automations to easily switch

**Note:** To switch themes via automations or the UI helpers below, go to your profile (**Settings** → **[your name]**) and set **Theme** to **Backend-selected**.

It is recommended to use [these automations (`basnijholt/home-assistant-config/automations/frontend.yaml`)](https://github.com/basnijholt/home-assistant-config/blob/master/automations/frontend.yaml) in combination with these helpers:
```yaml
input_select:
  theme:
    options:
      - blue-red
      - dark-blue
      - dark-green
      - light-blue
      - light-green
      - orange
      - red
    icon: mdi:format-color-fill
  
input_boolean:
  dark_mode:
    name: Dark mode
    icon: mdi:theme-light-dark
  theme_alternative:
    name: Theme alternative (disable active state color)
```

You can define these helpers in `configuration.yaml` as shown above, or create them via **Settings** → **Devices & Services** → **Helpers**. Then add `input_select.theme`, `input_boolean.theme_alternative`, and `input_boolean.dark_mode` to your dashboard.


## How does the code work

All the **28(!)** themes in [`themes/`](themes/) are **automatically generated** using [`create-themes.py`](create-themes.py) and the information in [`settings-light-dark.yaml`](settings-light-dark.yaml) is passed into [`template.jinja2`](template.jinja2).
The resulting file is [`themes/ios-themes.yaml`](themes/ios-themes.yaml) which contains all variants (different backgrounds and dark/light mode).

## HA 2025.5+ compatibility

This theme has been modernized to remove deprecated variables and add support
for UI components introduced in Home Assistant 2025.5.

**Removed** (Polymer/`paper-*` components were removed in HA 2025.5):
- `paper-slider-*` — sliders now follow `--primary-color` / `--accent-color` automatically
- `paper-toggle-button-*` — switches use `switch-checked-*` variables
- `paper-listbox-background-color`
- `paper-card-background-color`
- `paper-item-icon-color` / `paper-item-icon-active-color`
- Vaadin `--vaadin-text-field-*` input variables

**Updated:**
- `paper-dialog-background-color` → `dialog-background-color`

**Added** (view tab styling for `ha-tabs` / `sl-tab` in HA 2025.5+):
- `app-header-selection-bar-color` — active view tab indicator bar colour
- `sl-color-primary-600` — active view tab text/icon colour
- `sl-color-neutral-600` — inactive view tab text/icon colour

## HA 2026.4+ compatibility

HA 2026.4 migrated all input components from Material Design (`ha-textfield`)
to Web Awesome (`ha-input`) and introduced three new semantic form background
variables that default to `var(--ha-color-neutral-95)` — near-white (~#f2f2f2).

Without theme overrides, dark mode themes render `select` and other input
entity rows with a near-white background while `--primary-text-color` remains
`#FFF`, producing invisible white-on-white text.

## Changes

**`settings-light-dark.yaml`**
- Added `form_background_color` (light: `var(--secondary-background-color)`,
  dark: `var(--primary-background-color)`)

**`template.jinja2`**
- Added three new variables under `# Other`:
  - `ha-color-form-background`
  - `ha-color-form-background-hover`
  - `ha-color-form-background-disabled`

**`themes/ios-themes.yaml`**
- Regenerated
