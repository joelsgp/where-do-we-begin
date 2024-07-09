from datetime import datetime
from zoneinfo import ZoneInfo

import matplotlib.pyplot as plt

import download

TZ = ZoneInfo("America/New_York")


def get_days():
    feed = download.get_feed()
    published = [ep["published"] for ep in feed["episodes"]]
    release_day = [datetime.fromtimestamp(timestamp, tz=TZ).day for timestamp in published]

    return release_day


def main():
    release_day = get_days()
    bins = list(range(1, 31+1))

    fig, ax = plt.subplots()
    ax.hist(release_day, bins=bins)
    ax.set_xlabel("Day of the Month")
    ax.set_ylabel("Frequency")
    ax.set_title("Where Do We Begin Episode Release Days")
    ax.grid(True)

    fig.savefig("test.jpg")


if __name__ == "__main__":
    main()
