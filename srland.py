import os
import requests

while True:
    type, url = input().split(':')
    name = ''.join(url.split(".")[:-2])
    print(name)
    r = requests.get('https://starrailland.com/_next/static/media/'+url)
    if os.path.isdir(f"srland/{type}") == False:
        os.mkdir(f"srland/{type}")
    with open(f"srland/{type}/{name}.jpg", "wb") as f:
        f.write(r.content)