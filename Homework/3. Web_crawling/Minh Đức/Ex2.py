import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://dantri.com.vn/the-thao.htm").text 
soup = BeautifulSoup(html_text,"lxml")
content = soup.find_all("h3", class_ = "article-title") 

for index,test in enumerate (content):
    if index == 0: 
        result = test.find("a").text
        link =  test.a["href"]
        print(f"{index}.Front-page news: {result}\nLink: https://dantri.com.vn{link}")
    else : 
        result = test.find("a").text
        link =  test.a["href"]
        print(f"{index}.News: {result}\nLink: https://dantri.com.vn{link}")
