# YouTube Downloader

A simple Python script with a graphical user interface (GUI) that allows you to download videos from YouTube. The script uses `yt-dlp` (a modern alternative to `youtube-dl`) and `tkinter` for the GUI.

## Features

- Graphical user interface for entering download commands.
- Automatic clipboard retrieval for YouTube links.
- Supports downloading the best available video and audio in MP4 and M4A formats.

## Requirements

- Python 3.x
- `yt-dlp` (YouTube download tool)
- `pyperclip` (Clipboard management)
- `tkinter` (GUI toolkit)

## Installation

### macOS

1. **Install Homebrew** if it’s not already installed:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Install Python** (Python 3 is included by default):

    ```bash
    brew install python
    ```

3. **Install `yt-dlp`**:

    ```bash
    brew install yt-dlp
    ```

4. **Install Python dependencies**:

    ```bash
    pip3 install pyperclip
    ```

5. **(Optional) Install `tkinter`**:

    ```bash
    brew install python-tk
    ```

### Linux

1. **Install Python 3 and pip** (depending on your distribution):

    - **Debian/Ubuntu**:
        ```bash
        sudo apt update
        sudo apt install python3 python3-pip
        ```

    - **Fedora**:
        ```bash
        sudo dnf install python3 python3-pip
        ```

2. **Install `yt-dlp`**:

    ```bash
    pip3 install yt-dlp
    ```

3. **Install Python dependencies**:

    ```bash
    pip3 install pyperclip
    ```

4. **Install `tkinter`** (if needed):

    - **Debian/Ubuntu**:
        ```bash
        sudo apt install python3-tk
        ```

    - **Fedora**:
        ```bash
        sudo dnf install python3-tkinter
        ```

### Windows

1. **Install Python 3**:

    - Go to [python.org](https://www.python.org/downloads/) and download the Python installer.
    - Make sure to check the "Add Python to PATH" option and install Python.

2. **Install `yt-dlp`**:

    Open Command Prompt and run the following command:

    ```bash
    pip install yt-dlp
    ```

3. **Install Python dependencies**:

    ```bash
    pip install pyperclip
    ```

4. **`tkinter` should be included with Python**, but if it is missing, you can add it via the Python installer.

## Usage

1. **Clone the repository**:

    ```bash
    git clone https://github.com/in2d4rkn3zz/Python-YT-DLP/main/ytdownload.py.git
    cd youtube-downloader
    ```

2. **Run the script**:

    ```bash
    python ytdownload.py
    ```

3. **Usage**:

    - Copy the YouTube link you want to download to your clipboard.
    - Click the “Download” button in the GUI to start downloading the video.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
