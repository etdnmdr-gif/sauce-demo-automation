import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    # Указываем путь к твоему Chromium, так как он в нестандартном месте
    options.binary_location = r"C:\Users\Айнур\AppData\Local\Chromium\Application\chrome.exe"
    
    # Современный Selenium 4.11+ сам найдет драйвер, webdriver-manager не нужен
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()
