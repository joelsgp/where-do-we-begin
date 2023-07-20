import requests
from bs4 import BeautifulSoup, Tag

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


def filter_paragraphs(paragraph: Tag) -> bool:
    time_marker = paragraph.find("b")
    # keep the paragraph if it doesn't have a time marker
    return time_marker is None


def get_transcript(page_url: str) -> str:
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, features="html.parser")

    div_mw_content_text = soup.find("div", id="mw-content-text")
    span_transcript = div_mw_content_text.find("span", id="Transcript")
    h2_episode_list = span_transcript.parent

    paragraphs = h2_episode_list.find_next_siblings("p")
    paragraphs = filter(filter_paragraphs, paragraphs)

    paragraph_text = (p.text for p in paragraphs)
    joined = "\n".join(paragraph_text)

    return joined


def main():
    pages = get_page_list()
    qualified_pages = [URL_BASE + loc for loc in pages]
    transcript = get_transcript(qualified_pages[0])
    print(transcript)


if __name__ == "__main__":
    main()
