from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.locator import *


class LoginPage(object):
    def __init__(self, driver):
        # Инициализируем класс страницы LoginPage
        self.driver = driver
        self.locator = LoginPageLocator

    def wait_for_element(self, element):
        # Используем явное ожидание для поиска элемента
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(element))

    def enter_username(self, username):
        # Ввод username
        self.wait_for_element(self.locator.USERNAME)
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)
        print("Enter username")

    def enter_password(self, password):
        # Ввод password
        self.wait_for_element(self.locator.PASSWORD)
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)
        print("Enter password")

    def click_login_button(self):
        # Клик по кнопке Login
        self.wait_for_element(self.locator.LOGIN_BUTTON)
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()
        print("Click login button")

    def login(self, username, password):
        # Метод авторизации
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def login_with_valid_user(self):
        # Авторизация с валидными данными
        self.login("standard_user", "secret_sauce")
        return LoginPage(self.driver)
