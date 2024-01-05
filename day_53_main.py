from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

FORMS_LINK = YOUR_FORMS_LINK

URL = 'https://appbrewery.github.io/Zillow-Clone/'

# ----------------------------------------------------Beautiful Soup----------------------------------------------------
response = requests.get(URL)
zillow_clone_webpage = response.text
soup = BeautifulSoup(zillow_clone_webpage, 'html.parser')

links = soup.find_all('a')

for link in links:
    print(link.get('href'))

addresses = soup.find_all('address')

for address in addresses:
    print(address.get_text())

--------------------------------------------------Selenium Webdriver--------------------------------------------------
firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)
driver.get(URL)

property_list_element = driver.find_elements(By.CLASS_NAME, value='ListItem-c11n-8-84-3-StyledListCardWrapper')

for n in property_list_element:
    property_address = n.find_element(By.TAG_NAME, value='address')
    property_price = n.find_element(By.TAG_NAME, value='span')
    property_link = n.find_element(By.TAG_NAME, value='a')
    print(property_address.text)
    print(property_price.text.replace('$', '').replace('+', '').replace('/mo', '').replace('1 bd', '')
          .replace('1bd', ''))
    print(property_link.get_attribute('href'))

