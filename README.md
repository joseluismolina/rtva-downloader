# RTVA Downloader

A simple Python tool to download Canal Sur videos from m3u8 URLs using ffmpeg.

## Features

- **Simple**: Just provide the m3u8 URL from your browser
- **No re-encoding**: Downloads original quality
- **Cross-platform**: Works on Linux, macOS, and Windows
- **No dependencies**: Only requires ffmpeg

## Requirements

- **Python 3.7 or higher**
- **ffmpeg** (must be installed and in PATH)

### Install ffmpeg

**Ubuntu/Debian:**
```bash
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## Installation

```bash
# Clone the repository
git clone https://github.com/joseluismolina/rtva-downloader.git
cd rtva-downloader

# Or install with pip
pip install rtva-downloader
```

## Usage

### Step 1: Get the m3u8 URL

1. Open the video page in **Chrome** or **Firefox**
2. Press **F12** to open Developer Tools
3. Click the **Network** tab
4. Play the video (or reload the page with F5)
5. Look for a request ending in `.m3u8`
6. Right-click → **Copy** → **Copy URL**

The URL will look like:
```
https://cdn.rtva.interactvty.com/asrun_ott/.../.../playlist.m3u8
```

### Step 2: Download

```bash
python rtva_downloader.py "<m3u8_url>"

# Examples:
python rtva_downloader.py "https://cdn.rtva.interactvty.com/.../playlist.m3u8"
python rtva_downloader.py "<url>" -o "my_video.mp4"
python rtva_downloader.py "<url>" -o ~/Downloads/video.mp4
```

## Command Line Options

```
Usage: rtva_downloader.py <m3u8_url> [options]

Options:
  -o FILE       Output filename (default: video.mp4)
  -q QUALITY    Preferred quality: 1080p, 720p, 480p
  -n            Hide progress output
  -h, --help    Show help message
```

## Examples

```bash
# Basic download
python rtva_downloader.py "https://cdn.rtva.interactvty.com/.../playlist.m3u8"

# Save to specific location
python rtva_downloader.py "<url>" -o ~/Videos/andalucia_directo.mp4

# Hide progress ( quieter)
python rtva_downloader.py "<url>" -o output.mp4 -n
```

## Tips

- **m3u8 URLs expire quickly**: Download immediately after copying the URL
- **Different qualities**: If the m3u8 is a master playlist, ffmpeg downloads the best quality automatically
- **Browser extensions**: Use "Video DownloadHelper" or "Stream Detector" to find m3u8 URLs more easily

## Troubleshooting

**"ffmpeg not installed"**
- Install ffmpeg (see Requirements section)

**"Error opening input file"**
- The m3u8 URL may have expired. Get a fresh one from the browser

**Download interrupted**
- Partial files are automatically cleaned up. Just run the command again

## How It Works

This tool is a simple wrapper around **ffmpeg** that:
1. Takes an m3u8 URL (provided by you from the browser)
2. Uses ffmpeg to download all video segments
3. Merges them into a single MP4 file
4. Preserves original quality (no re-encoding)

## License

MIT License - See [LICENSE](LICENSE) file

## Disclaimer

This tool is for personal use only. Respect copyright laws and terms of service. Download only content you have the right to access.
