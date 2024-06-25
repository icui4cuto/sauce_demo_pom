from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.locator import *


class MainPage(object):
    def __init__(self, driver):
        # Инициализируем класс страницы MainPage
        self.driver = driver
        self.locator = MainPageLocator

    def wait_for_element(self, element):
        # Используем явное ожидание для поиска элемента
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(element))

    def add_product_to_cart(self, locator):
        # Добавляем товар в корзину
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()
        print("Add product to cart")

    def get_product_information(self, locator):
        # Получение информации о товаре
        self.wait_for_element(locator)
        return self.driver.find_element(*locator).text

    def go_to_cart(self):
        # Переход в корзину
        self.wait_for_element(self.locator.CART_BUTTON)
        self.driver.find_element(*self.locator.CART_BUTTON).click()
        print("Click cart button")

    def get_product_information_sauce_labs_backpack(self):
        # Получаем информацию о товаре 'sauce labs backpack'
        return (self.get_product_information(self.locator.SAUCE_LABS_BACKPACK_NAME),
                self.get_product_information(self.locator.SAUCE_LABS_BACKPACK_PRICE))

    def add_sauce_labs_backpack_to_cart(self):
        # Добавляем товар 'sauce labs backpack' в корзину
        self.add_product_to_cart(self.locator.SAUCE_LABS_BACKPACK_ADD_TO_CART)

