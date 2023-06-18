import json

import requests
from bs4 import BeautifulSoup



HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

url = "https://www.newmobilelife.com/wp-json/csco/v1/more-posts"

data_str = """action: csco_ajax_load_more
page: 3
posts_per_page: 30"""

data = {}
data_str_list = data_str.split("\n")  # ["action: csco_ajax_load_more", "page: 3", ...]
for row in data_str_list:
    # row = row.strip()
    key = row.split(": ")[0].strip()
    value = row.split(": ")[1].strip()
    data[key] = value

data = {
    row.split(": ")[0].strip(): row.split(": ")[1].strip()
    for row in data_str_list
}

data_list = [row.split(": ")[0].strip() for row in data_str_list]
print(data_list)

# print(data)

res = requests.post(url, headers=HEADERS, data=data, timeout=600)
# print(res.text)
json_data = res.json()
# json_data = json.loads(res.text)
# print(json_data)
html_str = json_data["data"]["content"]
soup = BeautifulSoup(html_str, "html.parser")
