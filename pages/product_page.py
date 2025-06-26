from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def is_product_list_loaded(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "inventory_item")) > 0
