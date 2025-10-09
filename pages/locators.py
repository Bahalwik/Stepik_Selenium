from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.LINK_TEXT, 'http://selenium1py.pythonanywhere.com/ru/accounts/login/')
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD_2 = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, '.row h1')
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'form[id=add_to_basket_form] button')
    BASKET_MESSAGES_BLOCK = (By.CSS_SELECTOR, '#messages strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.row p[class="price_color"]')


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a')
    EMPTY_BASKET = (By.CSS_SELECTOR, 'basket-items')
    EMPY_TEXT_BASKET = (By.CSS_SELECTOR, '#content_inner p')


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

