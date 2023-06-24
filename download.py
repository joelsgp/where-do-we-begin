from datetime import datetime
from typing import NamedTuple

import bs4
import requests


# todo publish module for easy future users?
# ok nvm scratch this file and try this instead
# https://github.com/gpodder/podcastparser


URL_RSS = "https://feed.podbean.com/wayneradiotv/feed.xml"


class Episode(NamedTuple):
    title: str
    description: str
    link: str
    timestamp: datetime
    mp3_url: str
    jpg_url: str


Episodes = list[Episode]
Items = list[bs4.Tag]


def get_items() -> Items:
    response = requests.get(URL_RSS)
    soup = bs4.BeautifulSoup(response.content, features="html.parser")

    channel = soup.find("channel")
    items = channel.find_all("item")

    return items


def episodes_from_items(items: Items) -> Episodes:
    episodes = []
    for it in items:
        enclosure = it.find("enclosure")
        mp3_url = enclosure.attrs["url"]

        image = it.find("itunes:image")
        jpg_url = image.attrs["href"]

        ep = Episode(mp3_url, jpg_url)
        episodes.append(ep)

    return episodes


def download(url: str, file_path: str):
    with requests.get(url, stream=True) as response:
        with open(file_path, "wb") as file:
            for chunk in response.iter_content:
                file.write(chunk)


def download_episode(episode: Episode):
    mp3_url = episode.mp3_url
    mp3_path = "test.mp3"  # todo
    download(mp3_url, mp3_path)

    jpg_url = episode.jpg_url
    jpg_path = "test.jpg"  # todo
    download(jpg_url, jpg_path)

    # todo fuse em with ffmpeg


# todo main functions
