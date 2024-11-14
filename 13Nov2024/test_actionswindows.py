import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_actions():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    firstname=driver.find_element(By.XPATH, "//input[@name='firstname']")
    #firstname.send_keys("thetestingacademy")
    actions=ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(firstname,"the testing academy").key_up(Keys.SHIFT).perform()
    time.sleep(2)