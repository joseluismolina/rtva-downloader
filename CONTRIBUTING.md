# Contributing to RTVA Downloader

Thank you for your interest in contributing to RTVA Downloader! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

- A clear title and description
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, ffmpeg version)
- The URL you were trying to download (if applicable)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- A clear description of the enhancement
- Why this would be useful
- Any implementation ideas you have

### Pull Requests

1. Fork the repository
2. Create a new branch from `main`: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test your changes
5. Commit your changes: `git commit -m 'Add some feature'`
6. Push to the branch: `git push origin feature/your-feature-name`
7. Open a Pull Request

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Add comments for complex logic

### Testing

Before submitting a PR:

1. Test the tool with different URLs
2. Verify it works on your platform
3. Check that ffmpeg is properly detected
4. Test error handling

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/rtva-downloader.git
cd rtva-downloader

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## Code of Conduct

- Be respectful and constructive
- Focus on what's best for the community
- Welcome newcomers and help them learn
- Show empathy towards others

## Questions?

Feel free to open an issue with your question or contact the maintainers.

Thank you for contributing! 🎉
