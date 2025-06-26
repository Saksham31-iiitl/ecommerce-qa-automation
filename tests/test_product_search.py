from pages.login_page import LoginPage
from pages.product_page import ProductPage

def test_product_display(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login()
    login_page.login("standard_user", "secret_sauce")

    product_page = ProductPage(driver)
    assert product_page.is_product_list_loaded()
