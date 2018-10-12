import unittest

from nose.plugins.attrib import attr
from selenium import webdriver

from letskodeit.settings import BASE_URL
from letskodeit.tests.locators import Locators


class LetsKodeIt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

        cls.driver.get(BASE_URL)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @attr('test')
    def test_select_from_dropdown(self):
        select_element = self.driver.find_element(*Locators.SELECT_DROPDOWN)
        select_element.click()

        options = select_element.find_elements(*Locators.OPTIONS)

        for option in options:
            if option.text.lower() == 'honda':
                option.click()
                break
        # option_selected = False

        for option in options:
            if option.text == 'honda':
                assert option.get_attribute('selected')
                break
