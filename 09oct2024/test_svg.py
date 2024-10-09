import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait


def test_open_vwoapp():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    time.sleep(6)
    states=driver.find_elements(By.XPATH, "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in states:
        print(state.get_attribute("aria-label"))
        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            time.sleep(10)
            break
