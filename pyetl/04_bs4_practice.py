import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/joke/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

# print(res.text)

# a = 1
# str(a)

soup = BeautifulSoup(res.text)

# print(soup)
title_tag = soup.findAll('a', {'id': 'logo'})
title_tag = soup.findAll('a', id='logo')  # [<a href="/bbs/" id="logo">批踢踢實業坊</a>]
# title_tag = soup.find('a', id='logo')  # <a href="/bbs/" id="logo">批踢踢實業坊</a>
# title_tag = soup.findAll('a')
print(title_tag)

title_tag = soup.select('a[id="logo"]')  # [<a href="/bbs/" id="logo">批踢踢實業坊</a>]
title_tag = soup.select('a#logo')  # [<a href="/bbs/" id="logo">批踢踢實業坊</a>]
# title_tag = soup.select_one('a#logo')  # <a href="/bbs/" id="logo">批踢踢實業坊</a>

print(title_tag)
print(title_tag[0])
print(title_tag[0].text)  # 批踢踢實業坊
print("https://www.ptt.cc" + title_tag[0]["href"])



