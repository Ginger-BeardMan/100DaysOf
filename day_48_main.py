from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open after program finishes
firefox_options = webdriver.FirefoxOptions()
# chrome_options.add_experimental_option('detach', True)

driver = webdriver.Firefox(options=firefox_options)

driver.get('https://python.org')

nums = [0, 1, 2, 3, 4]

keys = ['time', 'name', 'time', 'name', 'time', 'name', 'time', 'name', 'time', 'name']

full_list = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

item_list = full_list.text.split('\n')

upcoming_events = {num: {k: v for (k, v) in (keys, item_list)} for num in nums}

print(upcoming_events)

# rand_dict = {key: value for (key, value) in zip(keys, item_list)}
#
# print(rand_dict)

# driver.close()
# driver.quite()


# # PRACTICE CODE # #

# driver.get('https://www.amazon.com/Ultra-Sharp-Diamond-Sharpening-Stone/dp/B00SK3LDBE/ref=as_li_ss_tl?ie=UTF8&sr'
#            '=8-13&keywords=diamond+stone&linkId=90f4e83f38af9a75007c65a020859a74&language=en_US')
#
# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print(f'The price is {price_dollar.text}.{price_cents.text}')

# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute('placeholder'))
#
# button = driver.find_element(By.ID, value='submit')
# print(button.size)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
