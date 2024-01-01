from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

URL = 'http://orteil.dashnet.org/experiments/cookie/'

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)
driver.get(URL)

actionChains = ActionChains(driver)


def cookie_clicker():
    cookie_time = True
    start_time = time.time()
    while cookie_time:
        click_cookie = driver.find_element(By.ID, value='cookie')

        cookie_clicks = driver.find_element(By.XPATH, value='//*[@id="money"]')
        cookie_money = int(cookie_clicks.text)

        time_machine_element = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b')
        time_machine_money = int(time_machine_element.text.split()[3].replace(',', ''))
        time_machine_button = driver.find_element(By.ID, value="buyTime machine")

        portal_element = driver.find_element(By.XPATH, value='//*[@id="buyPortal"]/b')
        portal_money = int(portal_element.text.split()[2].replace(',', ''))
        portal_button = driver.find_element(By.ID, value='buyPortal')

        alchemy_lab_element = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b')
        alchemy_lab_money = int(alchemy_lab_element.text.split()[3].replace(',', ''))
        alchemy_lab_button = driver.find_element(By.ID, value='buyAlchemy lab')

        shipment_element = driver.find_element(By.XPATH, value='//*[@id="buyShipment"]/b')
        shipment_money = int(shipment_element.text.split()[2].replace(',', ''))
        shipment_button = driver.find_element(By.ID, value='buyShipment')

        mine_element = driver.find_element(By.XPATH, value='//*[@id="buyMine"]/b')
        mine_money = int(mine_element.text.split()[2].replace(',', ''))
        mine_button = driver.find_element(By.ID, value='buyMine')

        factory_element = driver.find_element(By.XPATH, value='//*[@id="buyFactory"]/b')
        factory_money = int(factory_element.text.split()[2].replace(',', ''))
        factory_button = driver.find_element(By.ID, value='buyFactory')

        grandma_element = driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]/b')
        grandma_money = int(grandma_element.text.split()[2].replace(',', ''))
        grandma_button = driver.find_element(By.ID, value='buyGrandma')

        cursor_element = driver.find_element(By.XPATH, value='//*[@id="buyCursor"]/b')
        cursor_money = int(cursor_element.text.split()[2].replace(',', ''))
        cursor_button = driver.find_element(By.ID, value='buyCursor')

        click_cookie.click()

        stop_time = time.time()

        if stop_time - start_time >= 600:
            cookie_time = False
        elif stop_time - start_time >= 5:
            if int(cookie_clicks.text) >= time_machine_money:
                time_machine_button.click()
            elif int(cookie_clicks.text) >= portal_money:
                portal_button.click()
            elif int(cookie_clicks.text) >= alchemy_lab_money:
                alchemy_lab_button.click()
            elif int(cookie_clicks.text) >= shipment_money:
                shipment_button.click()
            elif int(cookie_clicks.text) >= mine_money:
                mine_button.click()
            elif int(cookie_clicks.text) >= factory_money:
                factory_button.click()
            elif int(cookie_clicks.text) >= grandma_money:
                grandma_button.click()
            elif int(cookie_clicks.text) >= cursor_money:
                cursor_button.click()


cookie_clicker()
