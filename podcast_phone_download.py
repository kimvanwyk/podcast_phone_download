import requests
from bs4 import BeautifulSoup

import os 

BASEDIR = "podcasts"

res = requests.get("http://192.168.1.230:8000")
soup = BeautifulSoup(res.text, "html.parser")
links = [link.get("href") for link in soup.find_all("a") if "mp3" in link.get("href")]
for link in links:
    print(f"Downloading {link}")
    with requests.get(f"http://192.168.1.230:8000/{link}", stream=True) as res:
        with open(os.path.join(BASEDIR, link), 'wb') as f:
            for chunk in res.iter_content(chunk_size=8192):
                f.write(chunk)
