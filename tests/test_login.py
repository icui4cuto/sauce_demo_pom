from base.base_test import BaseTest
from pages.login_page import LoginPage


class TestLogin(BaseTest):
    def test_login_with_valid_user(self):
        """ Проверка возможности авторизации с валидными данными """
        login_page = LoginPage(self.driver)
        login_page.login_with_valid_user()
        self.assertIn("inventory.html", self.driver.current_url)




