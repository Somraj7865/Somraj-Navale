import time
from telnetlib import EC

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_actions():
    driver=webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    time.sleep(3)
    # closepopopup=driver.find_element(By.XPATH, "//span[@data-cy='closeModal']")
    #
    #
    # time.sleep(3)
    # closepopopup.click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-cy='closeModal']"))
    ).click()

    fromcity=driver.find_element(By.ID, "fromCity")

    #time.sleep(2)

    actions=ActionChains(driver)
    actions.move_to_element(fromcity).double_click().send_keys("Mumbai").send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    time.sleep(30)
