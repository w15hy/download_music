# pyright: reportAttributeAccessIssue=false

import eyed3
import musicbrainzngs
import requests

musicbrainzngs.set_useragent("metadata", "0.1", "fingerprint@gmail.com")


def metadata(id: str, file: str):
    recording = musicbrainzngs.get_recording_by_id(
        id, includes=["artists", "releases"]
    )["recording"]

    if recording is not None or "":
        info = get_metadata1(recording)
    else:
        info = get_metadata2()

    return set_metadata(*info, file)  # pyright: ignore


def get_album_official(recording: dict) -> str | None:
    for release in recording["release-list"]:
        if release["status"].lower() == "official":
            album = release["title"]
            return album
    return None


def set_metadata(title, artist, album, cover, file):
    # load the file
    audiofile = eyed3.load(file)

    if audiofile is not None:
        # add metadata
        audiofile.tag.artist = artist
        audiofile.tag.album = album
        audiofile.tag.album_artist = artist
        audiofile.tag.title = title

        # only remove the thumbnail from yt_dlp if there is no cover
        if cover:
            audiofile.tag.images.remove("Album cover")
            # add cover
            audiofile.tag.images.set(3, cover, "image/jpeg", "cover")

        # save
        audiofile.tag.save()

    return [artist, title]


def get_metadata1(recording: dict) -> list:
    title = recording["title"]
    artist = recording["artist-credit"][0]["artist"]["name"]
    album = get_album_official(recording)
    cover = get_image(recording)

    return [title, artist, album, cover]


def get_image(recording: dict):
    # iterate in all the reeases
    for release in recording["release-list"]:
        try:
            rid = release["id"]
            images = musicbrainzngs.get_image_list(rid)
            url = ""

            # verify that there is a img
            if "images" in images and len(images["images"]) > 0:
                img = images["images"][0]
                url = img["image"]

            # if url exist then download get the content
            if url:
                return requests.get(url).content

        except Exception:
            continue

    return None


def get_metadata2() -> list:
    title = input("Title: ")
    artist = input("Artist: ")
    album = input("Album: ")
    cover = None

    return [title, artist, album, cover]


def test():
    get_metadata2()


if __name__ == "__main__":
    test()
