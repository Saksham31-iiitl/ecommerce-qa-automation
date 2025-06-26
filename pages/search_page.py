from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def is_product_present(self, product_name):
        product_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for product in product_elements:
            if product_name.lower() in product.text.lower():
                return True
        return False

    def get_all_product_names(self):
        return [el.text for el in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]

    def sort_by_price_low_to_high(self):
        sort_dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_dropdown.click()
        sort_dropdown.find_element(By.XPATH, "//option[text()='Price (low to high)']").click()
