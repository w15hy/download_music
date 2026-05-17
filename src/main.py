#!/usr/bin/env python3
import os

import download as dl
import fingerprint as fp
import metadata as mtd


def ask_url() -> str | None:
    try:
        return input("Enter the URL you wish to download: ").strip()
    except KeyboardInterrupt:
        print("\n\nSe ha cerrado el programa")
        return None


def main():

    # Asks the user for a URL
    url = ask_url()

    while True:
        # verify if user enter the URL
        if not url or url == "":
            print("No URL provided.")
            return

        # starts the download
        file_path = ""
        if dl.out_dir:
            ydl_opts = dl.build_ydl_opts(dl.out_dir)
            file_path = dl.download(url, ydl_opts)

        # obatain recording_id
        if file_path:
            recording_id = fp.fingerprint(file_path)
            artist, title = mtd.metadata(recording_id, file_path)
            os.rename(file_path, f"{os.path.dirname(file_path)}/{artist} - {title}.mp3")

        url = ask_url()

        if url == "":
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSe ha cerrado el programa")
        exit()
