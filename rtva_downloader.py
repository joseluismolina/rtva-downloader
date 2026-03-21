#!/usr/bin/env python3
"""
RTVA Downloader - Canal Sur Video Downloader
Downloads HLS video streams from m3u8 URLs

Author: joseluismolina
License: MIT

Usage:
    python rtva_downloader.py <m3u8_url>
    python rtva_downloader.py <m3u8_url> -o ~/Videos
"""

import subprocess
import argparse
import sys
from pathlib import Path

__version__ = "1.0.0"


def check_ffmpeg():
    """Check if ffmpeg is installed"""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def download_video(m3u8_url, output_file="video.mp4", show_progress=True):
    """Download HLS stream using ffmpeg"""
    
    if not check_ffmpeg():
        print("ERROR: ffmpeg not installed!")
        print("Install with:")
        print("  Ubuntu/Debian: sudo apt install ffmpeg")
        print("  macOS: brew install ffmpeg")
        print("  Windows: https://ffmpeg.org/download.html")
        return False
    
    # Ensure .mp4 extension
    if not output_file.endswith('.mp4'):
        output_file += '.mp4'
    
    print(f"RTVA Downloader v{__version__}")
    print("=" * 60)
    print(f"Downloading: {m3u8_url}")
    print(f"Output: {output_file}")
    print("=" * 60)
    
    cmd = [
        'ffmpeg',
        '-hide_banner',
        '-loglevel', 'info' if show_progress else 'warning',
        '-stats',
        '-i', m3u8_url,
        '-c', 'copy',           # Copy without re-encoding
        '-bsf:a', 'aac_adtstoasc',
        '-y',                   # Overwrite if exists
        output_file
    ]
    
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        
        if show_progress:
            for line in process.stdout:
                print(line, end='')
        
        process.wait()
        
        if process.returncode == 0:
            print(f"\nDownload complete: {output_file}")
            return True
        else:
            print(f"\nError: ffmpeg exited with code {process.returncode}")
            return False
            
    except KeyboardInterrupt:
        print("\nDownload cancelled by user")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Download Canal Sur videos from m3u8 URLs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
HOW TO USE:
  1. Open the video page in Chrome/Firefox
  2. Press F12 → Network tab
  3. Play the video (or reload page)
  4. Find the request ending in .m3u8
  5. Right-click → Copy → Copy URL
  6. Run: python rtva_downloader.py "<m3u8_url>"

EXAMPLE:
  python rtva_downloader.py "https://cdn.rtva.interactvty.com/asrun_ott/.../playlist.m3u8"

OPTIONS:
  -o FILE       Output filename (default: video.mp4)
  -q QUALITY    Preferred quality: 1080p, 720p, 480p (optional)
  -n            Hide progress output
        """
    )
    
    parser.add_argument('url', help='m3u8 URL from browser Network tab')
    parser.add_argument('-o', '--output', default='video.mp4',
                       help='Output filename (default: video.mp4)')
    parser.add_argument('-q', '--quality', help='Preferred quality (1080p, 720p, 480p)')
    parser.add_argument('-n', '--no-progress', action='store_true',
                       help='Hide download progress')
    
    args = parser.parse_args()
    
    success = download_video(args.url, args.output, not args.no_progress)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
