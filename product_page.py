from base_page import BasePage
from locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_btn.click()

    def should_be_correct_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert product_name == message_name, (
            f"Expected product name '{product_name}' in success message, got '{message_name}'"
        )

    def should_be_correct_basket_total_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE_PRICE).text
        assert product_price == basket_price, (
            f"Expected basket total '{product_price}', got '{basket_price}'"
        )