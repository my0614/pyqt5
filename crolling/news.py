import requests
from bs4 import BeautifulSoup


source = requests.get("https://news.naver.com/").text
soup = BeautifulSoup(source, "html.parser")
hotKeys = soup.select(".keyword")
i=1
for i in 10:
    print(hotKeys[i].text)