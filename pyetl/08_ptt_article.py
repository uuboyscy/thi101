import requests
from bs4 import BeautifulSoup

from crawler_utils import load_article_to_some_folder

url = "https://www.ptt.cc/bbs/joke/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

for _ in range(5):
    res = requests.get(url, headers=headers, timeout=60)

    soup = BeautifulSoup(res.text, "html.parser")

    title_tag_list = soup.select('div.title a')

    # Get article title, url, and content, then load to a text file
    for title_tag in title_tag_list:  # <a href="/bbs/joke/M.1685841631.A.FEA.html">[趣事] Hebe告五人</a>
        title = title_tag.text
        article_url = "https://www.ptt.cc" + title_tag["href"]
        print(title)
        print(article_url)

        try:
            load_article_to_some_folder(
                article_url=article_url,
                file_name=title.replace("/", " ")
            )
        except OSError as e:
            print(e)
        except Exception as e:
            print(e)

    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]
