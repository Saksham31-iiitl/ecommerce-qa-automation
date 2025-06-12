from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    # Locators (edit as per your site's HTML if needed)
    BILLING_CONTINUE_BTN = (By.ID, "button-payment-address")
    SHIPPING_CONTINUE_BTN = (By.ID, "button-shipping-address")
    SHIPPING_METHOD_CONTINUE_BTN = (By.ID, "button-shipping-method")
    AGREE_CHECKBOX = (By.NAME, "agree")
    PAYMENT_CONTINUE_BTN = (By.ID, "button-payment-method")
    CONFIRM_ORDER_BTN = (By.ID, "button-confirm")
    ORDER_SUCCESS_MSG = (By.CSS_SELECTOR, "#content h1")

    def __init__(self, driver):
        self.driver = driver

    def complete_billing(self):
        # Click continue on billing details step
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.BILLING_CONTINUE_BTN)
        ).click()

    def complete_shipping(self):
        # Click continue on shipping address step
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.SHIPPING_CONTINUE_BTN)
        ).click()

    def complete_shipping_method(self):
        # Click continue on shipping method step
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.SHIPPING_METHOD_CONTINUE_BTN)
        ).click()

    def agree_terms_and_continue(self):
        # Tick agree to terms and continue
        agree_checkbox = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.AGREE_CHECKBOX)
        )
        if not agree_checkbox.is_selected():
            agree_checkbox.click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.PAYMENT_CONTINUE_BTN)
        ).click()

    def confirm_order(self):
        # Click confirm order
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.CONFIRM_ORDER_BTN)
        ).click()

    def is_order_successful(self):
        # Verify order success message
        msg = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.ORDER_SUCCESS_MSG)
        ).text
        return "Your order has been placed" in msg
