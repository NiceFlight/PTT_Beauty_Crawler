from bs4 import BeautifulSoup
import requests
import os

url = "past the url"
headers = {"Cookie": "over18=1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; "
                         "Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) "
                         "Chrome/126.0.0.0 Safari/537.36"
           }
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, 'html.parser')
filename = soup.find_all("span", attrs={"class": "article-meta-value"})
dir_name = f"images/{filename[2].text}"
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
links = soup.find_all("a")
allow_name = ["jpg", "png", "jpeg", "gif"]
for link in links:
    imglink = link.get("href")
    if not imglink:
        continue
    filename = imglink.split("/")[-1]
    extension = imglink.split(".")[-1]
    if extension in allow_name:
        img = requests.get(imglink, headers=headers)
        with open(f"{dir_name}/{filename}", 'wb') as file:
            file.write(img.content)
            print(f"Downloading.....{filename}......")
