#!/usr/bin/env python

import podcastparser
import requests

URL_RSS = "https://feed.podbean.com/wayneradiotv/feed.xml"


def get_episodes() -> list[dict]:
    url = URL_RSS
    # https://podcastparser.readthedocs.io/en/latest/#example
    # https://podcastparser.readthedocs.io/en/latest/#podcastparser.parse
    with requests.get(url, stream=True) as response:
        response.raw.decode_content = True
        parsed = podcastparser.parse(url, response.raw)

    episodes = parsed["episodes"]
    return episodes


def download(url: str, file_path: str):
    with requests.get(url, stream=True) as response:
        with open(file_path, "wb") as file:
            for chunk in response.iter_content():
                file.write(chunk)


def download_episode(episode: dict):
    title = episode["title"]
    print(f"doing episode '{title}'")

    mp3_url = episode["enclosures"][0]["url"]
    mp3_path = f"{title}.mp3"
    # easier to skip on spag entirely
    print("downloading audio")
    download(mp3_url, mp3_path)
    print("downloaded audio")

    jpg_url = episode["episode_art_url"]
    jpg_path = f"{title}.jpg"
    print("downloading image")
    download(jpg_url, jpg_path)
    print("downloaded image")

    # todo fuse em with ffmpeg
    # todo embed metadata - author,, date etc.


def main():
    print("getting episode list")
    episodes = get_episodes()
    print("got episode list")
    for ep in episodes:
        download_episode(ep)


if __name__ == "__main__":
    main()
