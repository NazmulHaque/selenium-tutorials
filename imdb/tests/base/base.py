import unittest

from selenium import webdriver

from imdb import settings
from imdb.pages.home.home_page import HomePage
from imdb.pages.search_result.search_result_page import SearchResultPage


class UIAutomationBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        runs very beginning of the test suite and runs for once only
        :return:
        """
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

        cls.home_page = HomePage(cls.driver)
        cls.search_result_page = SearchResultPage(cls.driver)

        cls.driver.get(settings.BASE_URL)

    @classmethod
    def tearDownClass(cls):
        """
        runs after finishing all test cases and runs for once
        :return:
        """
        cls.driver.quit()
