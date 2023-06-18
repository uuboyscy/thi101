import json

import requests


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

url = "https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6172841"

res = requests.get(url, headers=HEADERS, timeout=600)

# print(res.text)
json_data = json.loads(res.text)
# json_data = json.load(open("test.json", "r"))  # ByteIO
# print(json_data)

news_list = json_data["data"]["newsList"]
for news in news_list:
    print(news)

