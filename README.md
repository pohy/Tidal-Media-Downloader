<br>
    <a href="https://github.com/yaronzz/Tidal-Media-Downloader-PRO">[GUI-REPOSITORY]</a>
<br>

![Tidal-Media-Downloader](https://socialify.git.ci/yaronzz/Tidal-Media-Downloader/image?description=1&font=Rokkitt&forks=1&issues=1&language=1&name=1&owner=1&pattern=Circuit%20Board&stargazers=1&theme=Dark)

<div align="center">
  <h1>Tidal-Media-Downloader</h1>
  <a href="https://github.com/yaronzz/Tidal-Media-Downloader/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/yaronzz/Tidal-Media-Downloader.svg?style=flat-square" alt="">
  </a>
  <a href="https://github.com/yaronzz/Tidal-Media-Downloader/releases">
    <img src="https://img.shields.io/github/v/release/yaronzz/Tidal-Media-Downloader.svg?style=flat-square" alt="">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/github/issues/yaronzz/Tidal-Media-Downloader.svg?style=flat-square" alt="">
  </a>
  <a href="https://github.com/yaronzz/Tidal-Media-Downloader">
    <img src="https://img.shields.io/github/downloads/yaronzz/Tidal-Media-Downloader/total?label=tidal-gui%20download" alt="">
  </a>
  <a href="https://pypi.org/project/tidal-dl/">
    <img src="https://img.shields.io/pypi/dm/tidal-dl?label=tidal-dl%20download" alt="">
  </a>
  <a href="https://github.com/yaronzz/Tidal-Media-Downloader/actions/workflows/build.yml">
    <img src="https://github.com/yaronzz/Tidal-Media-Downloader/actions/workflows/build.yml/badge.svg" alt="">
  </a>
</div>
<p align="center">
  «Tidal-Media-Downloader» is an application that lets you download videos and tracks from Tidal. It supports two version: tidal-dl and tidal-gui. (This repository only contains tidal-dl, and the release isn't the newest gui version.)
    <br>
        <a href="https://github.com/yaronzz/Tidal-Media-Downloader-PRO/releases">Download</a> |
        <a href="https://doc.yaronzz.com/post/tidal_dl_installation/">Documentation</a> |
        <a href="https://doc.yaronzz.com/post/tidal_dl_installation_chn/">中文文档</a> |
    <br>
</p>

## 📺 Installation

```shell
pip3 install tidal-dl --upgrade
```

| USE                                                   | FUNCTION                   |
| ----------------------------------------------------- | -------------------------- |
| tidal-dl                                              | Show interactive interface |
| tidal-dl -h                                           | Show help-message          |
| tidal-dl -l "https://tidal.com/browse/track/70973230" | Download link              |
| tidal-dl -g                                           | Show simple-gui            |

If you are using windows system, you can use [tidal-pro](https://github.com/yaronzz/Tidal-Media-Downloader-PRO)

### Nightly Builds

| Download nightly builds from continuous integration: | [![Build Status][Build]][Actions] |
| ---------------------------------------------------- | --------------------------------- |

[Actions]: https://github.com/yaronzz/Tidal-Media-Downloader/actions
[Build]: https://github.com/yaronzz/Tidal-Media-Downloader/workflows/Tidal%20Media%20Downloader/badge.svg

## 🤖 Features

- Download album \ track \ video \ playlist \ artist-albums

- Add metadata to songs

- Selectable video resolution and track quality

## 💽 User Interface

<img src="https://i.loli.net/2020/08/19/gqW6zHI1SrKlomC.png" alt="image" style="zoom: 50%;" />

![image-20220708105823257](https://s2.loli.net/2022/07/08/vV6HsxugwoDyGr8.png)

![image-20200806013705425](https://i.loli.net/2020/08/06/sPLowIlCGyOdpVN.png)

## Settings - Possible Tags

### Album

| Tag               | Example value                       |
| ----------------- | ----------------------------------- |
| {ArtistName}      | The Beatles                         |
| {AlbumArtistName} | The Beatles                         |
| {Flag}            | M/A/E (Master/Dolby Atmos/Explicit) |
| {AlbumID}         | 55163243                            |
| {AlbumYear}       | 1963                                |
| {AlbumTitle}      | Please Please Me (Remastered)       |
| {AudioQuality}    | LOSSLESS                            |
| {DurationSeconds} | 1919                                |
| {Duration}        | 31:59                               |
| {NumberOfTracks}  | 14                                  |
| {NumberOfVideos}  | 0                                   |
| {NumberOfVolumes} | 1                                   |
| {ReleaseDate}     | 1963-03-22                          |
| {RecordType}      | ALBUM                               |
| {None}            |                                     |

### Track

| Tag               | Example Value                              |
| ----------------- | ------------------------------------------ |
| {TrackNumber}     | 01                                         |
| {ArtistName}      | The Beatles                                |
| {ArtistsName}     | The Beatles                                |
| {TrackTitle}      | I Saw Her Standing There (Remastered 2009) |
| {ExplicitFlag}    | (_Explicit_)                               |
| {AlbumYear}       | 1963                                       |
| {AlbumTitle}      | Please Please Me (Remastered)              |
| {AudioQuality}    | LOSSLESS                                   |
| {DurationSeconds} | 173                                        |
| {Duration}        | 02:53                                      |
| {TrackID}         | 55163244                                   |

### Video

| Tag            | Example Value      |
| -------------- | ------------------ |
| {VideoNumber}  | 00                 |
| {ArtistName}   | DMX                |
| {ArtistsName}  | DMX, Westside Gunn |
| {VideoTitle}   | Hood Blues         |
| {ExplicitFlag} | (_Explicit_)       |
| {VideoYear}    | 2021               |
| {TrackID}      | 188932980          |

## ☕ Support

If you really like my projects and want to support me, you can buy me a coffee and star this project.

<a href="https://www.buymeacoffee.com/yaronzz" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/arial-orange.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>

## 🎂 Contributors

This project exists thanks to all the people who contribute.

<a href="https://github.com/yaronzz/Tidal-Media-Downloader/graphs/contributors"><img src="https://contributors-img.web.app/image?repo=yaronzz/Tidal-Media-Downloader" /></a>

## 🎨 Libraries and reference

- [aigpy](https://github.com/yaronzz/AIGPY)
- [python-tidal](https://github.com/tamland/python-tidal)
- [redsea](https://github.com/redsudo/RedSea)
- [tidal-wiki](https://github.com/Fokka-Engineering/TIDAL/wiki)

## 📜 Disclaimer

- Private use only.
- Need a Tidal-HIFI subscription.
- You should not use this method to distribute or pirate music.
- It may be illegal to use this in your country, so be informed.

## 🔧 Building from Source

### Prerequisites

- Python 3.7 or higher
- Git

### Setup Virtual Environment

1. **Clone the repository:**

   ```shell
   git clone https://github.com/yaronzz/Tidal-Media-Downloader.git
   cd Tidal-Media-Downloader
   ```

2. **Create and activate virtual environment:**

   **Windows:**

   ```shell
   python -m venv .venv --prompt tidal-dl
   .venv\Scripts\activate
   ```

   **Linux/macOS:**

   ```shell
   python3 -m venv .venv --prompt tidal-dl
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```shell
   pip install -r TIDALDL-PY/requirements.txt
   ```

### Build Executable

The project includes an automated build script that handles virtual environment detection, dependency installation, and executable creation:

```shell
python build.py
```

**What the build script does:**

- ✅ Automatically detects and uses virtual environment
- ✅ Installs required build tools (wheel, pyinstaller)
- ✅ Sets up correct Python paths for imports
- ✅ Creates Python package (sdist & wheel)
- ✅ Generates standalone executable with PyInstaller
- ✅ Places final executable in `TIDALDL-PY/exe/tidal-dl.exe`

**Manual Build Steps** (if needed):

```shell
cd TIDALDL-PY
python setup.py sdist bdist_wheel
python -m PyInstaller -F tidal_dl/__init__.py
```

### Development Setup

For development and testing:

```shell
# Activate virtual environment first
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/macOS

# Install in development mode
cd TIDALDL-PY
pip install -e .

# Run directly
python -m tidal_dl
```
