from urllib import request


url = "https://34fc-35-234-26-40.ngrok-free.app/hello_get"

res = request.urlopen(url=url)

html = res.read().decode("utf-8")

print(html)
