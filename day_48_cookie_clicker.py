from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'http://orteil.dashnet.org/experiments/cookie/'

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)
driver.get(URL)

cookie_time = True

click_cookie = driver.find_element(By.ID, value='cookie')
cookie_clicks = driver.find_element(By.ID, value='money')

while cookie_time:
    click_cookie.click()
    if int(cookie_clicks.text) >= 20:
        cookie_time = False



