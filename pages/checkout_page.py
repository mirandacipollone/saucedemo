from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def enter_checkout_info(self, first_name, last_name, postal_code):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def get_error_message(self):
        return self.find(self.ERROR_MESSAGE).text

    def validate_total(self):
        # Extract values from the checkout overview page.
        item_total_label = self.find((By.CLASS_NAME, "summary_subtotal_label")).text  
        tax_label = self.find((By.CLASS_NAME, "summary_tax_label")).text               
        total_label = self.find(self.TOTAL_PRICE).text                                 
        
        # Convert text to float values.
        item_total = float(item_total_label.split("$")[-1])
        tax = float(tax_label.split("$")[-1])
        total_calculated = item_total + tax
        displayed_total = float(total_label.split("$")[-1])
        
        # Check that the calculated total is within an acceptable range.
        return abs(total_calculated - displayed_total) < 0.01
