from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    products_page = ProductsPage(driver)
    assert products_page.find(products_page.SORT_DROPDOWN)

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    error_text = login_page.get_error_message()
    assert error_text != ""  # Optionally, check for specific error text