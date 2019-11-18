# iOS Dark Mode Theme

[![Action Status](https://github.com/basnijholt/lovelace-ios-dark-mode-theme/workflows/yamllint/badge.svg)](https://github.com/basnijholt/lovelace-ios-dark-mode-theme/actions)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

> The iOS Dark Mode Theme by @basnijholt and modified from @kalkih's [Gist](https://gist.github.com/kalkih/fbe84b371ef7f992c3bd51b235e2c299)

## Screenshots

### Overview

![Theme - Overview](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-overview.jpg)
![Theme - Overview 2](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-overview-2.jpg)

### Map

![Theme - Map](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-map.jpg)

### Hass.io

![Theme - Hass.io](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-hassio.jpg)

### History

![Theme - History](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-history.jpg)

### Developer Tools

![Theme - Developer Tools](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-developer-tools.jpg)

### Configuration

![Theme - Configuration](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-configuration.jpg)

### Profile

![Theme - Profile](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-profile.jpg)

## Installation

1. Add the following code to your `configuration.yaml` file (reboot required).

```yaml
frontend:
  ... # your configuration.
  themes: !include_dir_merge_named themes
  ... # your configuration.
```

2. Move [backgrounds folder](backgrounds) to `/config/www/`.

3. Add the following line to your `lovelace-ui.yaml` or use the RAW editor:
```yaml
background: var(--background-image)
```

4. (Optional) add the following to the same file to make the header smaller (you need to install [cch](https://github.com/maykar/compact-custom-header) too):
```yaml
cch:
  background: rgba(155,155,155,.25)
  clock_format: 24
  options: clock
  swipe_animate: fade
  swipe_prevent_default: true
```

### HACS

1. Go to the Community Store.
2. Search for `iOS Dark Mode`.
3. Navigate to `iOS Dark Mode` theme.
4. Press `Install`.

### Manual

Clone this repository in your existing (or create it) `themes/` folder.

```bash
cd themes/
git clone https://github.com/basnijholt/lovelace-ios-dark-mode-theme.git
```

Or using submodules:

```bash
cd themes/
git submodule add https://github.com/basnijholt/lovelace-ios-dark-mode-theme.git
```
