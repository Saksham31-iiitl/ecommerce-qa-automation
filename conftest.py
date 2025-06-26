import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.headless = False  # So you can see the browser open
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
