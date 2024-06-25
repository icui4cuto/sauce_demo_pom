from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.locator import *


class YourInformationPage(object):
    def __init__(self, driver):
        # Инициализируем класс страницы YourInformation
        self.driver = driver
        self.locator = YourInformationLocator

    def wait_for_element(self, element):
        # Используем явное ожидание для поиска элемента
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(element))

    def enter_first_name(self, first_name):
        # Вводим имя клиента
        self.wait_for_element(self.locator.FIRST_NAME)
        self.driver.find_element(*self.locator.FIRST_NAME).send_keys(first_name)
        print("Enter first name")

    def enter_last_name(self, last_name):
        # Вводим фамилию клиента
        self.wait_for_element(self.locator.LAST_NAME)
        self.driver.find_element(*self.locator.LAST_NAME).send_keys(last_name)
        print("Enter last name")

    def enter_postal_code(self, postal_code):
        # Вводим почту клиента
        self.wait_for_element(self.locator.POSTAL_CODE)
        self.driver.find_element(*self.locator.POSTAL_CODE).send_keys(postal_code)
        print("Enter postal code")

    def enter_client_information(self):
        self.enter_first_name("Ivan")
        self.enter_last_name("Ivanov")
        self.enter_postal_code("123456")
        return YourInformationPage(self.driver)

    def go_to_overview(self):
        # Переход в 'overview'
        self.wait_for_element(self.locator.OVERVIEW_BUTTON)
        self.driver.find_element(*self.locator.OVERVIEW_BUTTON).click()
        print("Click overview button")
