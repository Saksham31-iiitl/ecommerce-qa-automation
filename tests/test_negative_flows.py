from pages.login_page import LoginPage

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login()
    login_page.login("invalid_user", "wrong_pass")
    assert "Epic sadface" in login_page.get_error_message()
