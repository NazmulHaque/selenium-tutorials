from imdb.pages.search_result.locators import SearchResultPageLocators
from common.waits import DriverWaits


class SearchResultPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_wait = DriverWaits(self.driver)

    def get_result_list(self):
        movies = self.driver.find_elements(*SearchResultPageLocators.LIST_ITEM)

        movie_names = []
        for movie in movies:
            movie_names.append(movie.text)

        # list comprehensive
        # movie_names = [movie.text for movie in movies]

        return movie_names
