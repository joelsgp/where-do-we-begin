import pyperclip

from download import get_episodes
from download_transcripts import get_page_list


episodes = get_episodes(False)
page_list = get_page_list()

number = 1
for ep in episodes:
    if ep["number"] != number:
        continue
    input(number)

    episode_link = ep["link"]
    page = page_list[number - 1]

    description = f"""{episode_link}

{page}

Playlist with info:
https://www.youtube.com/playlist?list=PLnKVDZ8hWc28qn1rmbvuR1Kbbj0wYwQJO"""

    print(description)
    pyperclip.copy(description)
