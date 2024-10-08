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
    driver.get("https://app.vwo.com/#/login")
    time.sleep(2)
    username_web_element=driver.find_element(By.NAME, "username").send_keys("admin@admin.com")
    time.sleep(2)
    password_web_element=driver.find_element(By.CSS_SELECTOR, "[data-qa='jobodapuxe']").send_keys("fhfgh")
    time.sleep(5)
    sign_web_element=driver.find_element(By.ID, "js-login-btn").click()
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibilty_of_element_located((By.ID, 'js-notification-box-msg'))
    )
    error_web_element=driver.find_element(By.ID,'js-notification-box-msg')
    assert error_web_element.text == "Your email, password, IP address or location did not match"
    time.sleep(5)

 #   assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"