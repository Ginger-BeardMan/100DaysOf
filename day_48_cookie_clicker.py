from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

URL = 'http://orteil.dashnet.org/experiments/cookie/'

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)
driver.get(URL)

cookie_time = True

# ------------------------------------------------------- Items -------------------------------------------------------
click_cookie = driver.find_element(By.ID, value='cookie')

cookie_clicks = driver.find_element(By.ID, value='money')
cookie_money = int(cookie_clicks.text)

# elder_pledge_element = driver.find_element(By.XPATH, value='//*[@id="buyElder Pledge"]/b')
# elder_pledge = int(elder_pledge_element.text.split()[1])

time_machine_element = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b')
time_machine = int(time_machine_element.text.split()[3].replace(',', ''))

portal_element = driver.find_element(By.ID, value='//*[@id="buyPortal"]/b')
portal = int(portal_element.text.split()[2].replace(',', ''))

alchemy_lab_element = driver.find_element(By.ID, value='//*[@id="buyAlchemy lab"]/b')
alchemy_lab = int(alchemy_lab_element.text.split()[3].replace(',', ''))

shipment_element = driver.find_element(By.ID, value='//*[@id="buyShipment"]/b')
shipment = int(shipment_element.text.split()[2].replace(',', ''))

mine_element = driver.find_element(By.ID, value='//*[@id="buyMine"]/b')
mine = int(mine_element.text.split()[2].replace(',', ''))

factory_element = driver.find_element(By.ID, value='//*[@id="buyFactory"]/b')
factory = int(factory_element.text.split()[2].replace(',', ''))

grandma_element = driver.find_element(By.ID, value='//*[@id="buyGrandma"]/b')
grandma = int(grandma_element.text.split()[2].replace(',', ''))

cursor_element = driver.find_element(By.ID, value='//*[@id="buyCursor"]/b')
cursor = int(cursor_element.text.split()[2].replace(',', ''))


def check_costs():
    sleep(300)
    if cookie_money >= time_machine:
        time_machine_element.click()
    elif cookie_money >= portal:
        portal_element.click()
    elif cookie_money >= alchemy_lab:
        alchemy_lab_element.click()
    elif cookie_money >= shipment:
        shipment_element.click()
    elif cookie_money >= mine:
        mine_element.click()
    elif cookie_money >= factory:
        factory_element.click()
    elif cookie_money >= grandma:
        grandma_element.click()
    elif cookie_money >= cursor:
        cursor_element.click()


while cookie_time:
    click_cookie.click()
    check_costs()
    if cookie_money >= 1000000:
        cookie_time = False
