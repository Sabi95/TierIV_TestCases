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
    # Log in to LinkedIn with VALID credentials
    login(driver, VALID_EMAIL, VALID_PASSWORD)
    # Confirm there is no error message
    print ("Logged in Successfully")

def test_invalid_login(driver):
    # Log in to LinkedIn with INVALID credentials
    login(driver, INVALID_EMAIL, INVALID_PASSWORD)
    # Confirm login FAIL by finding error message
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'form__label--error'))
    )
    assert error_message is not None
