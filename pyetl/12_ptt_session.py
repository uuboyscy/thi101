import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

landing_page_url = "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
over18_url = "https://www.ptt.cc/ask/over18"  # post
url = "https://www.ptt.cc/bbs/Gossiping/index.html"

data = {
    "from": "/bbs/Gossiping/index.html",
    "yes": "yes",
}

ss = requests.session()
print(ss.cookies)

ss.get(landing_page_url, headers=headers)
print(ss.cookies)

ss.post(over18_url, data=data, headers=headers)
print(ss.cookies)

res = ss.get(url, headers=headers)
print(ss.cookies)

# print(res.text)
