import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Youtube credentials
VALID_EMAIL = 't70323534@gmail.com'
VALID_PASSWORD = 'test123'
INVALID_PASSWORD = 'invalid123'
