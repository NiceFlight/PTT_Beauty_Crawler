from bs4 import BeautifulSoup
import requests
import os

url = "https://www.ptt.cc/bbs/Beauty/M.1628227703.A.D79.html"
headers = {"Cookie": "over18=1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; "
                         "Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) "
                         "Chrome/126.0.0.0 Safari/537.36"
           }
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, 'html.parser')
fileName = soup.find_all("span", attrs={"class": "article-meta-value"})
dirName = f"{fileName[2].text}"

if not os.path.exists(dirName):
    os.makedirs(dirName)
           
links = soup.find_all("a")
allowName = ["jpg", "png", "jpeg", "gif"]

for link in links:
    imgLink = link.get("href")
    if not imgLink:
        continue
    picName = imgLink.split("/")[-1]
    extension = imgLink.split(".")[-1]
    if extension in allowName:
        img = requests.get(imgLink, headers=headers)
        with open(f"{dirName}/{picName}", 'wb') as file:
            file.write(img.content)
            print(f"Downloading.....{picName}......")
