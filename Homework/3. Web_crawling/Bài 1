#bài 1: python script để tự động đăng nhập vào tài khoản github
import requests
from getpass import getpass
from bs4 import BeautifulSoup as bs

headers = {
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}

login_data = {
'commit': 'Sign in',
'utf8': '%E2%9C%93',
'login': input('Username: '),
'password': getpass()
}

url = 'https://github.com/session'
session = requests.Session()
response = session.get(url, headers=headers)

soup = bs(response.text, 'lxml')
login_data['authenticity_token'] = soup.find(
'input', attrs={'name': 'authenticity_token'})['value']
response = session.post(url, data=login_data, headers=headers)
response1 = session.get('https://github.com', headers=headers)

if response.url==response1.url:
    bsoup = bs(response1.content,'lxml')
    profile_img = bsoup.find("img",class_='avatar avatar-small circle')['src']
    print(profile_img)
else :
    print('login failed')
