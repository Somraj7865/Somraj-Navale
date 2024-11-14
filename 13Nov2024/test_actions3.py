import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_actions():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    # Wait for and close the popup
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-cy='closeModal']"))
    ).click()

    # Click on 'From' city input box
    from_city = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fromCity"))
    )
    from_city.click()

    # Enter 'Mumbai' and select it
    from_city_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='From']"))
    )
    from_city_input.send_keys("Mumbai")
    time.sleep(2)  # brief wait for suggestions to load

    # Press down arrow and then enter to select
    from_city_input.send_keys(Keys.ARROW_DOWN)
    from_city_input.send_keys(Keys.ENTER)

    time.sleep(5)  # wait to see the action before closing
    driver.quit()

test_actions()
