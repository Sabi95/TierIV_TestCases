import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Youtube credentials
VALID_EMAIL = 't70323534@gmail.com'
VALID_PASSWORD = 'test1234!'
INVALID_PASSWORD = 'invalid123'


@pytest.fixture(scope="module")
def driver():
    # Initialize Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # Quit driver after test
    driver.quit()

def test_valid_login(driver):
    # Open Youtube page
    driver.get('https://www.youtube.com')
    # Navigate to login page
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape'))
    )
    login_button.click()
    # Enter valid email
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
    )
    username_input.send_keys(VALID_EMAIL)
    # Click 'Next' button
    username_next= WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'identifierNext'))
    )
    username_next.click()
    # Enter valid password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    )
    password_input.send_keys(VALID_PASSWORD)
    # Click 'Next' button
    password_next= WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'passwordNext'))
    )
    password_next.click()
    # Confirm successful login by finding profile icon
    profile_pic = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="header-bar"]/header/div/ytm-topbar-menu-button-renderer/button/ytm-profile-icon/img'))
    )
    assert profile_pic is not None