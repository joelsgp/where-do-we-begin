#!/usr/bin/env python

from datetime import date, datetime
from zoneinfo import ZoneInfo

import matplotlib.pyplot as plt

import download

TZ = ZoneInfo("America/New_York")
# bunch got imported on this date at the start of the feed
EXCLUDE_DATE = date(year=2018, month=12, day=10)


def get_days(feed: dict) -> list[int]:
    published = [ep["published"] for ep in feed["episodes"]]
    release_date = (datetime.fromtimestamp(timestamp, tz=TZ) for timestamp in published)
    release_date = (d for d in release_date if d.date() != EXCLUDE_DATE)
    release_day = [d.day for d in release_date]

    return release_day


def main():
    print("downloading..")
    feed = download.get_feed()
    print("downloaded")
    release_day = get_days(feed)

    current_date = datetime.now(tz=TZ).strftime("%Y-%m-%d")
    latest_title = feed["episodes"][0]["title"]
    print(latest_title)

    bins = list(range(1, 31 + 1))
    print("making plot..")
    fig, ax = plt.subplots()
    ax.hist(release_day, bins=bins)
    ax.set_xlabel("Day of the Month")
    ax.set_ylabel("Frequency")
    ax.set_title(
        "Where Do We Begin Episode Release Days\n"
        # f"As of {current_date}\n"
        "Latest episode:\n"
        f"{latest_title}"
    )
    ax.grid(True)

    print("saving plot..")
    fig.savefig("test.jpg")
    print("saved")


if __name__ == "__main__":
    main()
