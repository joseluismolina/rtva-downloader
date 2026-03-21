#!/usr/bin/env python3
"""Setup script for RTVA Downloader"""

from setuptools import setup
from pathlib import Path

readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="rtva-downloader",
    version="1.0.0",
    author="joseluismolina",
    description="Download Canal Sur videos from m3u8 URLs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joseluismolina/rtva-downloader",
    py_modules=["rtva_downloader"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "rtva-downloader=rtva_downloader:main",
        ],
    },
    keywords="rtva canal-sur video downloader hls m3u8",
    project_urls={
        "Bug Reports": "https://github.com/joseluismolina/rtva-downloader/issues",
        "Source": "https://github.com/joseluismolina/rtva-downloader",
    },
)
