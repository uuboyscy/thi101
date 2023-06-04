import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/joke/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

title_tag_list = soup.select('div.title a')

# print(title_tag_list)
for title_tag in title_tag_list:  # <a href="/bbs/joke/M.1685841631.A.FEA.html">[趣事] Hebe告五人</a>
    title = title_tag.text
    article_url = "https://www.ptt.cc" + title_tag["href"]
    print(title)
    print(article_url)
