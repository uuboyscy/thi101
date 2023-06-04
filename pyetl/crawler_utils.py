"""Crawler utils."""
import os

import requests
from bs4 import BeautifulSoup

FOLDER_PATH = "./ptt"
if not os.path.exists(FOLDER_PATH):
    os.mkdir(FOLDER_PATH)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def load_article_to_some_folder(article_url: str, file_name: str) -> None:
    """Request article url and load it to file."""
    res = requests.get(article_url, headers=headers, timeout=60)
    soup = BeautifulSoup(res.text, "html.parser")
    article_tag = soup.select_one('div[id="main-content"]')

    for tag_name in ["div", "a", "span"]:
        for tag in article_tag.select(tag_name):
            tag.extract()

    article = article_tag.text

    # with open("%s/%s.txt" % (FOLDER_PATH, file_name), "w", encoding="utf-8") as f:
    with open(f"{FOLDER_PATH}/{file_name}.txt", "w", encoding="utf-8") as f:
        f.write(article)


if __name__ == "__main__":
    load_article_to_some_folder(
        "https://www.ptt.cc/bbs/joke/M.1685851563.A.F2B.html",
        "[耍冷] 推特上在夯什麼 Part.1170",
    )
