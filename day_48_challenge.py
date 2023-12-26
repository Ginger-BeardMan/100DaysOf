from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'http://secure-retreat-92358.herokuapp.com/'

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)
driver.get(URL)

first_name_input = driver.find_element(By.NAME, value='fName')
first_name_input.send_keys('John')

last_name_input = driver.find_element(By.NAME, value='lName')
last_name_input.send_keys('Smith')

email_input = driver.find_element(By.NAME, value='email')
email_input.send_keys('johnsmith@gmail.com')

send_button = driver.find_element(By.CSS_SELECTOR, value='form button')
send_button.click()
