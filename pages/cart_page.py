from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[data-test^='remove']")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def remove_product(self, product_name=None):
        if product_name:
            remove_locator = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='cart_item']//button")
            self.click(remove_locator)
        else:
            self.click(self.REMOVE_BUTTON)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

