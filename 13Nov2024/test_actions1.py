import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys


def test_actions():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    atag=driver.find_element(By.XPATH, "//a[@id='click']")
    time.sleep(2)
    atag.click()
    time.sleep(3)

    action_builders=ActionBuilder(driver)
    action_builders.pointer_action.pointer_up(MouseButton.BACK)
    action_builders.perform()
    time.sleep(2)