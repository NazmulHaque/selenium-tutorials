from imdb.pages.home.locators import HomePageLocators
from imdb.pages.search_result.locators import SearchResultPageLocators
from imdb.common.waits import DriverWaits


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_wait = DriverWaits(self.driver)

    def search_by_keyword(self, query_string):
        # import pdb; pdb.set_trace()

        search_box = self.driver.find_element(*HomePageLocators.SEARCH_BOX)
        search_box.send_keys(query_string)

        search_button = self.driver.find_element(*HomePageLocators.SEARCH_BUTTON)
        search_button.click()

        self.driver_wait.wait_till_element_visible(SearchResultPageLocators.FIND_HEADER)

