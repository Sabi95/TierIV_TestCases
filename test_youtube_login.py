import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# LinkedIn credentials
VALID_EMAIL = 't70323534@gmail.com'
VALID_PASSWORD = 'test123'
INVALID_EMAIL = 'invalidemail@test.com'
INVALID_PASSWORD = 'invalid123'


@pytest.fixture(scope="module")
def driver():
    # Initialize Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # Quit driver after test
    driver.quit()

def login(driver, email, password):
    # Open LinkedIn login page
    driver.get('https://www.linkedin.com/login')
    # Identify email field and enter email
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )
    email_field.send_keys(email)
    # Identify password field and enter password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password_field.send_keys(password)
    # Identify login button and click 'Sign In' button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"]'))
    )
    login_button.click()

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
        EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button'))
    )
    username_input.send_keys(VALID_EMAIL)
    # Click 'Next' buttongit
    username_next= WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierId"]'))
    )
    username_next.click()
    # Enter valid password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    )
    password_input.send_keys(VALID_PASSWORD)
    # Click 'Next' button
    password_next= WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button'))
    )
    password_next.click()
    # Confirm successful login by finding profile icon
    profile_pic = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//yt-icon[@id="guide-icon"]'))
    )
    assert profile_pic is not None
