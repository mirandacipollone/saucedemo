from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.config import VALID_USERNAME, VALID_PASSWORD

def perform_login(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

def test_add_single_product(driver):
    perform_login(driver)
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart()
    assert products_page.get_cart_count() == 1

def test_add_multiple_products(driver):
    perform_login(driver)
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart(product_name="Sauce Labs Backpack")
    products_page.add_product_to_cart(product_name="Sauce Labs Bike Light")
    assert products_page.get_cart_count() == 2

def test_remove_product(driver):
    perform_login(driver)
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart()
    products_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.remove_product()
    cart_items = driver.find_elements(*cart_page.CART_ITEMS)
    assert len(cart_items) == 0