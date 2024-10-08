import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_vwoapp():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']").click()

    WebDriverWait(driver=driver, timeout=5).until(EC.url_contains("profile.php#login"))
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
