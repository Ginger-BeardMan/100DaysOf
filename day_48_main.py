from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(options=firefox_options)

driver.get('https://python.org')

event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_title = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
events = {}

for n in range(4):
    events[n] = {'time': event_times[n].text, 'name': event_title[n].text}

print(events)

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
