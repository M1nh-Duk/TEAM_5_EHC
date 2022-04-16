from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import getpass

# INput username and password
username = input("Enter your Username or Email address:\n> ")
password = getpass.getpass(prompt="Enter your Password:\n> ")
# Perform login action
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://github.com/login")
driver.find_element_by_id("login_field").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_name("commit").click()
#Check login 
errors = driver.find_elements_by_class_name("flash-error")
error_message = "Incorrect username or password."

if any(error_message in e.text for e in errors):
    print("Login failed!")
else:
    print("Login successfully!")
    html_text = driver.page_source
    soup = BeautifulSoup(html_text,'lxml')
    #Get username through image tag
    username1 = soup.find("img",class_="avatar avatar-user")["alt"]
   
    print(f"Your Github link is {driver.current_url}{username1[1:]}\nYour username is {username1[1:]}") 
    
    driver.close()
