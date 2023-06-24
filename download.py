#!/usr/bin/env python

import podcastparser
import requests

URL_RSS = "https://feed.podbean.com/wayneradiotv/feed.xml"


def get_episodes() -> dict:
    url = URL_RSS
    with requests.get(url, stream=True) as response:
        parsed = podcastparser.parse(url, response.raw)
    return parsed


def download(url: str, file_path: str):
    with requests.get(url, stream=True) as response:
        with open(file_path, "wb") as file:
            for chunk in response.iter_content():
                file.write(chunk)


def download_episode(episode: dict):
    # todo switch from object to podcastparser dict
    mp3_url = episode.mp3_url
    mp3_path = "test.mp3"  # todo
    download(mp3_url, mp3_path)

    jpg_url = episode.jpg_url
    jpg_path = "test.jpg"  # todo
    download(jpg_url, jpg_path)

    # todo fuse em with ffmpeg


def main():
    episodes = get_episodes()
    print(episodes)
    # for ep in episodes:
    # todo


if __name__ == "__main__":
    main()
