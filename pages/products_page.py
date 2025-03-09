from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class ProductsPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    BURGER_MENU_CLOSE = (By.ID, "react-burger-cross-btn")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_name=None):
        if product_name:
            product_locator = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
            self.click(product_locator)
        else:
            self.click(self.ADD_TO_CART_BUTTON)

    def get_cart_count(self):
        try:
            badge = self.find(self.CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0

    def sort_products(self, sort_option_value):
        dropdown = self.find(self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_value(sort_option_value)

    def open_cart(self):
        self.click(self.CART_LINK)

    def open_menu(self):
        self.click(self.BURGER_MENU)

    def close_menu(self):
        # If the close button is visible, click it
        self.click(self.BURGER_MENU_CLOSE)
