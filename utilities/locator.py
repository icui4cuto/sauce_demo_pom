from selenium.webdriver.common.by import By


class LoginPageLocator(object):
    USERNAME = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//button[@class='error-button']")


class MainPageLocator(object):
    SAUCE_LABS_BACKPACK_ADD_TO_CART = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    SAUCE_LABS_BACKPACK_NAME = (By.XPATH, "//div[contains(text(), 'Sauce Labs Backpack')]")
    SAUCE_LABS_BACKPACK_PRICE = (By.XPATH, "(//div[@data-test='inventory-item-price'])[1]")
    CART_BUTTON = (By.XPATH, "//a[@data-test='shopping-cart-link']")


class CartPageLocator(object):
    SAUCE_LABS_BACKPACK_NAME_IN_CART = (By.XPATH, "//div[contains(text(), 'Sauce Labs Backpack')]")
    SAUCE_LABS_BACKPACK_PRICE_IN_CART = (By.XPATH, "//div[@data-test='inventory-item-price']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@data-test='checkout']")


class YourInformationLocator(object):
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    POSTAL_CODE = (By.XPATH, "//input[@id='postal-code']")
    OVERVIEW_BUTTON = (By.XPATH, "//input[@id='continue']")


class OverviewLocator(object):
    SAUCE_LABS_BACKPACK_NAME_IN_OVERVIEW = (By.XPATH, "//div[@data-test='inventory-item-name']")
    SAUCE_LABS_BACKPACK_PRICE_IN_OVERVIEW = (By.XPATH, "//div[@data-test='inventory-item-price']")
    FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")
