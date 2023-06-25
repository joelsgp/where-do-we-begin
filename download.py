#!/usr/bin/env python


import urllib.request

import podcastparser


URLS_FILE = "urls.txt"
URL_RSS = "https://feed.podbean.com/wayneradiotv/feed.xml"

Episodes = list[dict]


def get_episodes() -> Episodes:
    feedurl = URL_RSS
    # https://podcastparser.readthedocs.io/en/latest/#example
    # https://podcastparser.readthedocs.io/en/latest/#podcastparser.parse
    parsed = podcastparser.parse(feedurl, urllib.request.urlopen(feedurl))

    episodes = parsed["episodes"]
    return episodes


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


# todo fuse em with ffmpeg
# todo embed metadata - author,, date etc.


# todo: could make a thing instead where it saves the podcast data to json
# then you can pick which one to merge by episode number, and it gets the file names from the json
# then does it!


def main():
    print("getting episode list")
    episodes = get_episodes()
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
