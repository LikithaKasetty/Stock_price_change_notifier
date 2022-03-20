from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from datetime import datetime as dt
import yagmail
import os

sender = 'xxxxx@gmail.com'
PASSWORD = 'tdejqgdfaskmizxe'
receiver = 'yyyyy@gmail.com'

def get_drvier():
    # Set options to make browsing easier
    options = Options()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options = options)
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver

def main():
   driver = get_drvier()
   element = driver.find_element(by="xpath", value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
   return element.text

vlaue = (main())
if float(vlaue[1 : -2]) < (+1.81):
    current_now = dt.now()
    subject = "Stock Value: " + str(current_now)
    contents = "Today's Stock value : " + vlaue
    yag = yagmail.SMTP(user=sender, password= PASSWORD)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
