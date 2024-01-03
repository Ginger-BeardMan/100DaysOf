from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

URL = 'https://appbrewery.github.io/Zillow-Clone/'

# ----------------------------------------------------Beautiful Soup----------------------------------------------------
response = requests.get(URL)
zillow_clone_webpage = response.text
soup = BeautifulSoup(zillow_clone_webpage, 'html.parser')


# --------------------------------------------------Selenium Webdriver--------------------------------------------------
firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)
driver.get(URL)
