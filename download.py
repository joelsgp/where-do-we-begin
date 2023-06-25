#!/usr/bin/env python


import json
import urllib.request
from datetime import datetime

import podcastparser


UPDATE_FEED = False

FEED_JSON_FILE = "feed.json"
URLS_FILE = "urls.txt"
URL_RSS = "https://feed.podbean.com/wayneradiotv/feed.xml"

Episodes = list[dict]


def get_feed() -> dict:
    feedurl = URL_RSS
    # https://podcastparser.readthedocs.io/en/latest/#example
    # https://podcastparser.readthedocs.io/en/latest/#podcastparser.parse
    parsed = podcastparser.parse(feedurl, urllib.request.urlopen(feedurl))
    return parsed


def sort_episodes(episodes: Episodes, reverse: bool = False):
    episodes.sort(key=lambda ep: ep["published"], reverse=reverse)


def get_download_urls(episodes: Episodes):
    urls = []
    for ep in episodes:
        mp3_url = ep["enclosures"][0]["url"]
        jpg_url = ep["episode_art_url"]
        urls.append(mp3_url)
        urls.append(jpg_url)

    return urls


def get_metadata_arguments(episode: dict, feed: dict) -> list[str]:
    mapping = {
        "artist": "itunes_author",
        "comment": "subtitle",
        "title": "title",
        "track": "number",
    }

    metadata = {}

    # from mapping
    for k, v in mapping.items():
        metadata[k] = episode[v]
    # constant
    metadata["album"] = "RTVS Podcasts"
    metadata["language"] = "eng"
    # special
    published = episode["published"]
    published_datetime = datetime.utcfromtimestamp(published)
    formatted = published_datetime.isoformat()
    metadata["date"] = formatted

    # make ffmpeg command line arguments
    args = []
    for k, v in metadata.items():
        args.append("-metadata")
        args.append(f"{k}={v}")

    return args


def main():
    print("getting episode list")
    if UPDATE_FEED:
        feed = get_feed()
        with open(FEED_JSON_FILE, "w") as file:
            json.dump(feed, file, indent=4)
            file.write("\n")
    else:
        with open(FEED_JSON_FILE) as file:
            feed = json.load(file)
    episodes = feed["episodes"]
    print("got episode list")

    print("writing download urls to file")
    sort_episodes(episodes)
    urls = get_download_urls(episodes)
    lines = (u + "\n" for u in urls)
    with open(URLS_FILE, "w") as file:
        file.writelines(lines)
    print("wrote download urls to file")


if __name__ == "__main__":
    main()
