from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

wiki_article_num = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')

print(wiki_article_num.text)
