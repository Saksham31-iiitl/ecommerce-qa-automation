from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_add_to_cart(driver):
    login = LoginPage(driver)
    login.go_to_login()
    login.login("standard_user", "secret_sauce")

    product_page = ProductPage(driver)
    product_page.add_to_cart()

    cart = CartPage(driver)
    cart.go_to_cart()

    assert "cart" in cart.driver.current_url
