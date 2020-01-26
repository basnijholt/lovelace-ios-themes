# iOS Themes

[![Action Status](https://github.com/basnijholt/lovelace-ios-themes/workflows/yamllint/badge.svg)](https://github.com/basnijholt/lovelace-ios-themes/actions)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
[![homeassistant_community](https://img.shields.io/badge/HA%20community-forum-brightgreen)](https://community.home-assistant.io/t/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX)
[![Github Stars](https://img.shields.io/github/stars/basnijholt/lovelace-ios-themes)](https://github.com/basnijholt/lovelace-ios-themes)

> The iOS Theme by @basnijholt and modified from @kalkih's [Gist](https://gist.github.com/kalkih/fbe84b371ef7f992c3bd51b235e2c299)

Offers alternatives to the [**iOS Dark Mode Theme**](https://github.com/basnijholt/lovelace-ios-dark-mode-theme)!

## Screenshots

### Overview

![Theme - Overview](https://raw.githubusercontent.com/basnijholt/lovelace-ios-themes/master/docs/theme-overview.jpg)

## Installation

1. Add the following code to your `configuration.yaml` file (reboot required).

```yaml
frontend:
  ... # your configuration.
  themes: !include_dir_merge_named themes
  ... # your configuration.
```

2. Add the following line to your `lovelace-ui.yaml` or use the RAW editor:
```yaml
background: var(--background-image)
```

3. (Optional) add the following to the same file to make the header smaller (you need to install [`custom-header`](https://github.com/maykar/custom-header) too):
```yaml
custom_header:
  background: 'rgba(155, 155, 155, 0.25)'
  compact_mode: true
  button_text:
    options: '{{ hours24 }}:{{ minutesLZ }}'
```

4. (Optional) change the background to a different one, see [`backgrounds/README.md`](https://github.com/basnijholt/lovelace-ios-themes/tree/master/backgrounds).

### HACS

1. Go to the Community Store.
2. Search for `iOS Themes`.
3. Navigate to `iOS Themes` theme.
4. Press `Install`.

### Manual

Clone this repository in your existing (or create it) `themes/` folder.

```bash
cd themes/
git clone https://github.com/basnijholt/lovelace-ios-themes.git
```

Or using submodules:

```bash
cd themes/
git submodule add https://github.com/basnijholt/lovelace-ios-themes.git
```

## Automations to easily switch
It is recommended to use [these automations (`basnijholt/home-assistant-config/automations/frontend.yaml`)](https://github.com/basnijholt/home-assistant-config/blob/master/automations/frontend.yaml) in combination with these:
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
```
Then add `input_select.theme` and `input_boolean.dark_mode` to your Lovelace UI.
