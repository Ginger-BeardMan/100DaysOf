from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.amazon.com/Ultra-Sharp-Diamond-Sharpening-Stone/dp/B00SK3LDBE/ref=as_li_ss_tl?ie=UTF8&sr'
#            '=8-13&keywords=diamond+stone&linkId=90f4e83f38af9a75007c65a020859a74&language=en_US')
#
# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print(f'The price is {price_dollar.text}.{price_cents.text}')

driver.get('https://python.org')
# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute('placeholder'))
#
# button = driver.find_element(By.ID, value='submit')
# print(button.size)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close()
# driver.quite()
