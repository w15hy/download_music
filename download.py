# pyright: reportAttributeAccessIssue=false
import logging
import os

import yt_dlp
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename="script.log", level=logging.INFO)

# Validate OUT_DIR
out_dir = os.getenv("OUT_DIR")
if not out_dir:
    raise ValueError("OUT_DIR missing from .env")
if not os.path.isdir(out_dir):
    raise NotADirectoryError(f"OUT_DIR is not a valid directory: {out_dir}")


def build_ydl_opts(out_dir: str) -> dict:
    return {
        "no_warnings": True,
        "format": "bestaudio/best",
        "restrictfilenames": True,
        "writethumbnail": True,
        "outtmpl": os.path.join(out_dir, "%(title)s.%(ext)s"),
        "quiet": True,
        "noplaylist": True,  # Download only one video if playlist
        "cookiesfrombrowser": ("firefox", None, None, None),
        # Extract audio and thumbnail using ffmpeg
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            },
            {"key": "EmbedThumbnail"},
            {
                "key": "FFmpegMetadata",
                "add_metadata": True,
            },
        ],
    }


def download(url: str, ydl_opts: dict) -> str | None:

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # pyright: ignore
        try:
            info_dict = ydl.extract_info(url, download=True)
            path_file = ydl.prepare_filename(info_dict)
            mp3_path = os.path.splitext(path_file)[0] + ".mp3"
            logging.info(
                f"Downloaded: {os.path.splitext(os.path.basename(mp3_path))[0]}"
            )
            return mp3_path
        except yt_dlp.utils.DownloadError as e:
            logging.error(f"Download failed: {e}")
            return None
        except Exception as e:
            logging.exception("Unexpected error:")
            return None


def test():
    # Asks the user for a URL
    url = input("Enter the URL you wish to download: ").strip()

    # verify if user enter the URL
    if not url or url == "":
        print("No URL provided.")
        return

    # starts the download
    if out_dir:
        ydl_opts = build_ydl_opts(out_dir)
        download(url, ydl_opts)


if __name__ == "__main__":
    test()
