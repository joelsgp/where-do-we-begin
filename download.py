import bs4
import requests

URL_RSS = "https://feed.podbean.com/wayneradiotv/feed.xml"

# mp3 url, jpg url
Episode = tuple[str, str]
Episodes = list[Episode]
Items = list[bs4.Tag]


def get_items() -> Items:
    response = requests.get(URL_RSS)
    soup = bs4.BeautifulSoup(response.content)

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

        ep = (mp3_url, jpg_url)
        episodes.append(ep)
    
    return episodes


def download_episode(episode: Episode):
    mp3_url, jpg_url = episode
    with requests.get(mp3_url, stream=True) as response:
        pass  # todo
