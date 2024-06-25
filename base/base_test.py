import time
import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    url = "https://www.saucedemo.com/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.url)
        print("Тест:", self.shortDescription(), "\nStart test!")

    def tearDown(self):
        time.sleep(5)
        print("Finish test!")
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
