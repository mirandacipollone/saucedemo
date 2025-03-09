from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import VALID_USERNAME, VALID_PASSWORD

def test_sort_low_to_high(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    products_page = ProductsPage(driver)
    products_page.sort_products("lohi")
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(el.text.replace("$", "")) for el in price_elements]
    assert prices == sorted(prices)