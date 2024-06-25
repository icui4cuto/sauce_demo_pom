from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.locator import *


class CartPage(object):
    def __init__(self, driver):
        # Инициализируем класс страницы CartPage
        self.driver = driver
        self.locator = CartPageLocator

    def wait_for_element(self, element):
        # Используем явное ожидание для поиска элемента
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(element))

    def get_product_information(self, locator):
        # Получение информации о товаре
        self.wait_for_element(locator)
        return self.driver.find_element(*locator).text

    def get_product_information_sauce_labs_backpack_in_cart(self):
        # Получаем информацию о товаре в корзине 'sauce labs backpack'
        return (self.get_product_information(self.locator.SAUCE_LABS_BACKPACK_NAME_IN_CART),
                self.get_product_information(self.locator.SAUCE_LABS_BACKPACK_PRICE_IN_CART))

    def go_to_your_information(self):
        # Переход в 'your information'
        self.wait_for_element(self.locator.CHECKOUT_BUTTON)
        self.driver.find_element(*self.locator.CHECKOUT_BUTTON).click()
        print("Click your information")