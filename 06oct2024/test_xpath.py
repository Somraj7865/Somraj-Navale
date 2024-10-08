import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import allure


def test_open_vwoapp():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(2)
    make_app_element=driver.find_element(By.ID, "//a[@id='btn-make-appointment']").click()
    #//a[contains(text(),'Make')]
    #//a[starts-with(text(),'App')]
    #btn-make-appointment - make_app_element=driver.find_element(By.CSS_SELECTOR,
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"