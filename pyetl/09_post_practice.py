import requests


url = "https://34fc-35-234-26-40.ngrok-free.app/hello_post"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

data = {
    "username": "asdfsdfgghdfghjgfh"
}

res = requests.post(url, headers=headers, data=data)

print(res.text)
