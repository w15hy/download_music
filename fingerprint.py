import os

import acoustid
from dotenv import load_dotenv
from readchar import key, readkey

_ = load_dotenv()

# Validate OUT_DIR
ACOUST_ID = os.getenv("ACOUST_ID")
if not ACOUST_ID:
    raise ValueError("ACOUST_ID missing from .env")


def nav_fingerprints(
    arr_score: list[float],
    arr_recording_id: list[str],
    arr_title: list[str],
    arr_artist: list[str],
    n: int,
) -> str:
    print(f"[{n}] Title:  {arr_title[n]}")
    print(f"{' '*3} Artist: {arr_artist[n]}")
    print(f"{' '*3} Score:  {arr_score[n]:.3f}")

    state = n
    k = readkey()

    if k == key.ENTER:
        print("Selected")
        return arr_recording_id[n]
    elif k == key.RIGHT and n != len(arr_title) - 1:
        state = state + 1
    elif k == key.LEFT and n != 0:
        state = state - 1

    print("\033[F\033[2K" * 3, end="")

    return nav_fingerprints(arr_score, arr_recording_id, arr_title, arr_artist, state)


def fingerprint(file: str):
    arr_score, arr_recording_id, arr_title, arr_artist = [], [], [], []
    for score, recording_id, title, artist in acoustid.match(ACOUST_ID, file):
        arr_score.append(score)
        arr_recording_id.append(recording_id)
        arr_title.append(title)
        arr_artist.append(artist)

    return nav_fingerprints(arr_score, arr_recording_id, arr_title, arr_artist, 0)


def test():
    print(
        fingerprint("/home/w15hy/Music/Avenged_Sevenfold_-_Hail_to_the_King_Ragnar.mp3")
    )


if __name__ == "__main__":
    test()
