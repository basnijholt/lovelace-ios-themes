# iOS Dark Mode Theme

[![Build Status](https://www.travis-ci.org/basnijholt/lovelace-ios-dark-mode-theme.svg?branch=master)](https://www.travis-ci.org/basnijholt/lovelace-ios-dark-mode-theme)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

> The iOS Dark Mode Theme by @basnijholt and modified from @kalkih's [Gist](https://gist.github.com/kalkih/fbe84b371ef7f992c3bd51b235e2c299)

## Screenshots

### Overview

![Theme - Overview](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-overview.png)

### Map

![Theme - Map](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-map.png)

### Logbook

![Theme - Logbook](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-logbook.png)

### History

![Theme - History](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-history.png)

### Developer Tools

![Theme - Developer Tools](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-developer-tools.png)

### Configuration

![Theme - Configuration](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-configuration.png)

### Profile

![Theme - Profile](https://raw.githubusercontent.com/basnijholt/lovelace-ios-dark-mode-theme/master/docs/theme-profile.png)

## Installation

Add the following code to your `configuration.yaml` file (reboot required).

```yaml
frontend:
  ... # your configuration.
  themes: !include_dir_merge_named themes
  ... # your configuration.
```

### HACS

1. Go to the Community Store.
2. Search for `iOS Dark Mode`.
3. Navigate to `iOS Dark Mode` theme.
4. Press `Install`.
5. Go to services and trigger the `frontend.reload_themes` service.

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
