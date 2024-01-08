from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

FORMS_URL = YOUR_FORMS_LINK

ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'

# ----------------------------------------------------Beautiful Soup----------------------------------------------------
response = requests.get(ZILLOW_URL)
zillow_clone_webpage = response.text
soup = BeautifulSoup(zillow_clone_webpage, 'html.parser')

links = []
addresses = []
prices = []

page_links = soup.find_all('a', {'class': 'property-card-link'})

for link in page_links:
    links.append(link.get('href'))

page_addresses = soup.find_all('address')

for address in page_addresses:
    addresses.append(address.get_text().replace('\n', '').lstrip().rstrip())

page_prices = soup.find_all('span', {'class': 'PropertyCardWrapper__StyledPriceLine'})

for price in page_prices:
    prices.append(price.get_text().replace('+', '').replace('/mo', '').replace('1 bd', '').replace('1bd', ''))

--------------------------------------------------Selenium Webdriver--------------------------------------------------
firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)
driver.get(FORMS_URL)

for n in range(44):
    q_1 = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/'
                                              'div[1]/div/div[1]/input')
    q_2 = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/'
                                              'div[1]/div/div[1]/input')
    q_3 = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/'
                                              'div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]'
                                                        '/div/span/span')
    q_1.send_keys(addresses[n])
    q_2.send_keys(prices[n])
    q_3.send_keys(links[n])
    submit_button.click()
    refresh_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    refresh_button.click()

# property_list_element = driver.find_elements(By.CLASS_NAME, value='ListItem-c11n-8-84-3-StyledListCardWrapper')

# for n in property_list_element:
#     property_address = n.find_element(By.TAG_NAME, value='address')
#     property_price = n.find_element(By.TAG_NAME, value='span')
#     property_link = n.find_element(By.TAG_NAME, value='a')
#     print(property_address.text)
#     print(property_price.text.replace('$', '').replace('+', '').replace('/mo', '').replace('1 bd', '')
#           .replace('1bd', ''))
#     print(property_link.get_attribute('href'))

