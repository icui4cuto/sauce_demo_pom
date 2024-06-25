from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.locator import *


class OverviewPage(object):
    def __init__(self, driver):
        # Инициализируем класс страницы Overview
        self.driver = driver
        self.locator = OverviewLocator

    def wait_for_element(self, element):
        # Используем явное ожидание для поиска элемента
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(element))

    def get_product_information(self, locator):
        # Получение информации о товаре на странице overview
        self.wait_for_element(locator)
        return self.driver.find_element(*locator).text

    def get_product_information_sauce_labs_backpack_in_overview(self):
        # Получаем информацию о товаре 'sauce labs backpack' на странице overview
        return (self.get_product_information(self.locator.SAUCE_LABS_BACKPACK_NAME_IN_OVERVIEW),
                self.get_product_information(self.locator.SAUCE_LABS_BACKPACK_PRICE_IN_OVERVIEW))

    def go_to_finish(self):
        # Переход в 'finish'
        self.wait_for_element(self.locator.FINISH_BUTTON)
        self.driver.find_element(*self.locator.FINISH_BUTTON).click()
        print("Click finish button")
