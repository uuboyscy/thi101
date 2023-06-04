from urllib import request


url = "https://www.ptt.cc/bbs/joke/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

req = request.Request(url=url, headers=headers)
# res = request.urlopen(url=url)
res = request.urlopen(req)

html = res.read().decode("utf-8")

print(html)
