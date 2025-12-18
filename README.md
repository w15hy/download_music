# 🎵 Music Downloader

A simple and efficient YouTube music downloader built with `yt-dlp` and `ffmpeg` for linux.  
It automatically converts videos into **MP3 (320 kbps)** and embeds the thumbnail as cover art.

---

## ✨ Features

- Downloads audio in the **best available quality**
- Converts audio to **MP3 320 kbps**
- Embeds the **video thumbnail as album art**
- Supports age-restricted videos via browser cookies
- Configurable through a `.env` file
- Automatic logging to file

---

## 🚀 Requirements

Make sure you have installed:

- Python 3.10+
- yt-dlp
- FFmpeg
- python-dotenv
- AcoustID API KEY

Install dependencies:

```bash
pip install -r requirements.txt
````

## ⚡ Usage

0. Config through .env

1. Run the program:
```bash
python main.py
````

2. When prompted, enter the URL you wish to download:

```
Enter the URL you wish to download: https://www.youtube.com/{video_or_audio}
```

*Note: You can provide a single URL or a list of URLs, but the program will only download one URL at a time — not the entire list.*

3. The program will automatically:

   * Validate the URL
   * Build the `yt-dlp` configuration
   * Start the download using your custom `download` module

4. If no URL is provided, the script will exit with:

```
No URL provided.
```
