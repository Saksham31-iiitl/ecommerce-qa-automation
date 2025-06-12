from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    LOGIN_LINK = (By.LINK_TEXT, "My Account")
    LOGIN_BUTTON = (By.LINK_TEXT, "Login")
    # ... other locators ...

    def __init__(self, driver):
        self.driver = driver

    def go_to_login(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.LOGIN_LINK)
        ).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.LOGIN_BUTTON)
        ).click()
