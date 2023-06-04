"""Crawler utils."""
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def load_article(article_url: str, file_name: str) -> None:
    """Request article url and load it to file."""
    res = requests.get(article_url, headers=headers, timeout=60)
    soup = BeautifulSoup(res.text, "html.parser")
    article_tag = soup.select_one('div[id="main-content"]')

    for tag_name in ["div", "a", "span"]:
        for tag in article_tag.select(tag_name):
            tag.extract()

    article = article_tag.text
    # print(article_tag)
    # print(article)
    print(soup)


if __name__ == "__main__":
    load_article(
        "https://www.ptt.cc/bbs/joke/M.1685851563.A.F2B.html",
        "[耍冷] 推特上在夯什麼 Part.1170",
    )
