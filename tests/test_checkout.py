from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout(driver):
    login = LoginPage(driver)
    login.go_to_login()
    login.login("standard_user", "secret_sauce")

    product_page = ProductPage(driver)
    product_page.add_to_cart()

    cart = CartPage(driver)
    cart.go_to_cart()

    checkout = CheckoutPage(driver)
    checkout.fill_information("John", "Doe", "12345")
    checkout.finish_checkout()

    assert "checkout-complete" in checkout.driver.current_url
