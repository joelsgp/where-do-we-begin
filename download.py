#!/usr/bin/env python


import json
import subprocess
import urllib.request
from datetime import datetime
from pathlib import Path

import podcastparser


UPDATE_FEED = False

DIRECTORY_DOWNLOADS = Path("downloads/")
DIRECTORY_MERGED = Path("merged/")
FEED_JSON_FILE = "feed.json"
URLS_FILE = "urls.txt"
URL_RSS = "https://feed.podbean.com/wayneradiotv/feed.xml"
SUFFIX_MERGED_VIDEO = ".mp4"

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


def get_metadata_arguments(episode: dict) -> list[str]:
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


def merge_episode(episode: dict):
    title = episode["title"]
    print(f"Merging episode {title}")

    # mp3 in
    mp3_url = episode["enclosures"][0]["url"]
    mp3_file_name = Path(mp3_url).name
    mp3_file_path = DIRECTORY_DOWNLOADS / mp3_file_name
    # jpg in
    jpg_url = episode["episode_art_url"]
    jpg_file_name = Path(jpg_url).name
    jpg_file_path = DIRECTORY_DOWNLOADS / jpg_file_name
    # mp4 out
    out_file_name = Path(title).with_suffix(SUFFIX_MERGED_VIDEO)
    out_file_path = DIRECTORY_MERGED / out_file_name

    metadata_args = get_metadata_arguments(episode)

    args = [
        "./merge-test.sh",
        mp3_file_path,
        jpg_file_path,
        out_file_path,
        *metadata_args,
    ]

    subprocess.run(args)
    print("merged episode")


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

    if UPDATE_FEED:
        print("writing download urls to file")
        sort_episodes(episodes)
        urls = get_download_urls(episodes)
        lines = (u + "\n" for u in urls)
        with open(URLS_FILE, "w") as file:
            file.writelines(lines)
        print("wrote download urls to file")

    print("merging all episodes")
    for ep in episodes:
        merge_episode(ep)
    print("merged all episodes")


if __name__ == "__main__":
    main()
