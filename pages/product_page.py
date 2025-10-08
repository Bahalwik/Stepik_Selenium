from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def check_info_after_add_to_basket(self):
        message_name = self.browser.find_elements(*ProductPageLocators.MESSAGES_BLOCK)[0].text
        message_price = self.browser.find_elements(*ProductPageLocators.MESSAGES_BLOCK)[2].text


        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text


        assert product_name == message_name, 'bad product name'
        assert product_price == message_price, 'bad product price'

