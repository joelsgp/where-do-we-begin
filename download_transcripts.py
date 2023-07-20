import requests
from bs4 import BeautifulSoup

URL_BASE = "https://wayneradiotv.fandom.com"


def get_page_list() -> list[str]:
    """Return a list of URLs to wiki pages for episodes."""
    list_url = "https://wayneradiotv.fandom.com/wiki/Where_Do_We_Begin%3F"

    response = requests.get(list_url)
    soup = BeautifulSoup(response.text, features="html.parser")

    div_mw_content_text = soup.find("div", id="mw-content-text")
    span_episode_list = div_mw_content_text.find("span", id="Episode_List")
    h2_episode_list = span_episode_list.parent
    ol = h2_episode_list.find_next_sibling("ol")

    hyperlinks = ol.find_all("a")
    page_list = [a.attrs["href"] for a in hyperlinks]

    return page_list


print(get_page_list())
