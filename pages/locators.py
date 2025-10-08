from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.LINK_TEXT, 'http://selenium1py.pythonanywhere.com/ru/accounts/login/')
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, '.row h1')
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'form[id=add_to_basket_form] button')
    MESSAGES_BLOCK = (By.CSS_SELECTOR, '#messages strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.row p[class="price_color"]')

