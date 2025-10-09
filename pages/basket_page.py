from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        login_link.click()

    def check_no_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET)

    def basket_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPY_TEXT_BASKET)
