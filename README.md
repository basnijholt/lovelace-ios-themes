# iOS Themes

[![Action Status](https://github.com/basnijholt/lovelace-ios-themes/workflows/yamllint/badge.svg)](https://github.com/basnijholt/lovelace-ios-themes/actions)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
[![homeassistant_community](https://img.shields.io/badge/HA%20community-forum-brightgreen)](https://community.home-assistant.io/t/ios-dark-and-light-mode-with-easy-background-change/206215)
[![Github Stars](https://img.shields.io/github/stars/basnijholt/lovelace-ios-themes)](https://github.com/basnijholt/lovelace-ios-themes)

> The iOS Theme by @basnijholt and modified from @kalkih's [Gist](https://gist.github.com/kalkih/fbe84b371ef7f992c3bd51b235e2c299)

A generalized version of [*iOS Dark Mode Theme*](https://github.com/basnijholt/lovelace-ios-dark-mode-theme)!
This includes both **Dark and Light Mode** and 7 different HomeKit backgrounds.
Installing this theme adds 28 different themes:
- `ios-dark-green`
- `ios-light-blue`
- `ios-light-green`
- `ios-orange`
- `ios-blue-red`
- `ios-red`
- `ios-dark-blue`
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

1. Installation of the themes with HACS.

* (If you do not have it yet) Install [HACS](https://hacs.xyz/docs/installation/manual).
* Go to the HACS Community Store.
* Click on the `THEMES` tab.
* Search and install the `iOS Themes`.

2. Add the following code to your `configuration.yaml` file (reboot required).

```yaml
frontend:
  ... # your configuration.
  themes: !include_dir_merge_named themes
  ... # your configuration.
```

3. Add the following line to your `lovelace-ui.yaml` or use the RAW editor:
```yaml
background: var(--background-image)
```

So the end result will be something like [this example](https://github.com/basnijholt/home-assistant-config/blob/master/lovelace-ui.yaml).

## Automations to easily switch
**WARNING: if you want to switch themes using automations, you need to go to your profile and select "Backend-selected" for Theme!**

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
  theme_alternative:
    name: Theme alternative (disable active state color)
```
Then add `input_select.theme`, `input_boolean.theme_alternative`, and `input_boolean.dark_mode` to your Lovelace UI.


## How does the code work

All the **28(!)** themes in [`themes/`](themes/) are **automatically generated** using [`create-themes.py`](create-themes.py) and the information in [`settings-light-dark.yaml`](settings-light-dark.yaml) is passed into [`template.jinja2`](template.jinja2).
The resulting file is [`themes/ios-themes.yaml`](themes/ios-themes.yaml) which contains all variants (different backgrounds and dark/light mode).
