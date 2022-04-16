#Bài 2: Crawl các title báo ở https://dantri.com.vn/the-thao.htm
from urllib import response
import requests
from bs4 import BeautifulSoup as bs

url = 'https://dantri.com.vn/the-thao.htm'
response = requests.get(url)
soup = bs(response.content , 'lxml')
tags = soup.find_all('h3')
for x in range(len(tags)):
    if x ==0 :
        title = tags[x].text
        link = tags[x].a["href"]
        print(f"{x}.Front-page news: {title}")
        print(f"Link: https://dantri.com.vn{link}\n")
    else :
        title = tags[x].find("a").text
        link = tags[x].a["href"]
        print(f"{x}.News: {title}")
        print(f"Link: https://dantri.com.vn{link}\n")
