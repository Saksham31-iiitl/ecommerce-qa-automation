import yaml
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

# Load config
with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(config["base_url"])
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login()
    login_page.login(config["username"], config["password"])
    assert "My Account" in driver.title
