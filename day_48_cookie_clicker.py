from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

URL = 'http://orteil.dashnet.org/experiments/cookie/'

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)
driver.get(URL)

actionChains = ActionChains(driver)

cookie_time = True

# ------------------------------------------------------- Items -------------------------------------------------------
click_cookie = driver.find_element(By.ID, value='cookie')

cookie_clicks = driver.find_element(By.ID, value='money')
cookie_money = int(cookie_clicks.text)

# elder_pledge_element = driver.find_element(By.XPATH, value='//*[@id="buyElder Pledge"]/b')
# elder_pledge = int(elder_pledge_element.text.split()[1])

time_machine_element = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b')
time_machine = int(time_machine_element.text.split()[3].replace(',', ''))

portal_element = driver.find_element(By.XPATH, value='//*[@id="buyPortal"]/b')
portal = int(portal_element.text.split()[2].replace(',', ''))

alchemy_lab_element = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b')
alchemy_lab = int(alchemy_lab_element.text.split()[3].replace(',', ''))

shipment_element = driver.find_element(By.XPATH, value='//*[@id="buyShipment"]/b')
shipment = int(shipment_element.text.split()[2].replace(',', ''))

mine_element = driver.find_element(By.XPATH, value='//*[@id="buyMine"]/b')
mine = int(mine_element.text.split()[2].replace(',', ''))

factory_element = driver.find_element(By.XPATH, value='//*[@id="buyFactory"]/b')
factory = int(factory_element.text.split()[2].replace(',', ''))

grandma_element = driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]/b')
grandma = int(grandma_element.text.split()[2].replace(',', ''))

cursor_element = driver.find_element(By.XPATH, value='//*[@id="buyCursor"]/b')
cursor = int(cursor_element.text.split()[2].replace(',', ''))


def check_costs():
    if cookie_money >= time_machine:
        actionChains.double_click(time_machine_element)
    elif cookie_money >= portal:
        actionChains.double_click(portal_element)
    elif cookie_money >= alchemy_lab:
        actionChains.double_click(alchemy_lab_element)
    elif cookie_money >= shipment:
        actionChains.double_click(shipment_element)
    elif cookie_money >= mine:
        actionChains.double_click(mine_element)
    elif cookie_money >= factory:
        actionChains.double_click(factory_element)
    elif cookie_money >= grandma:
        actionChains.double_click(grandma_element)
    elif cookie_money >= cursor:
        actionChains.double_click(cursor_element)


while cookie_time:
    click_cookie.click()
    check_costs()
    if cookie_money >= 1000000:
        cookie_time = False
