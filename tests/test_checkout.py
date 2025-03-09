from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import VALID_USERNAME, VALID_PASSWORD


def perform_login(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

def add_products(driver, count=3):
    products_page = ProductsPage(driver)
    for _ in range(count):
        products_page.add_product_to_cart()

def test_successful_checkout(driver, faker):
    perform_login(driver)
    add_products(driver, 3)
    products_page = ProductsPage(driver)
    products_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout() 
    checkout_page = CheckoutPage(driver)
    first_name = faker.first_name()
    last_name = faker.last_name()
    postal_code = faker.postcode()
    checkout_page.enter_checkout_info(first_name, last_name, postal_code)
    assert checkout_page.validate_total()
    checkout_page.finish_checkout()
    
    complete_header = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "THANK YOU" in complete_header.upper()

def test_checkout_missing_details(driver):
    perform_login(driver)
    add_products(driver, 3)
    products_page = ProductsPage(driver)
    products_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()
    
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_checkout_info("John", "", "12345")
    error_text = checkout_page.get_error_message()
    assert error_text != ""