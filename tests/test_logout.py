from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import VALID_USERNAME, VALID_PASSWORD, BASE_URL

def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    
    products_page = ProductsPage(driver)
    products_page.click(products_page.BURGER_MENU)
    logout_link = (By.ID, "logout_sidebar_link")
    products_page.click(logout_link)
    
    assert driver.current_url.rstrip("/") == BASE_URL.rstrip("/")