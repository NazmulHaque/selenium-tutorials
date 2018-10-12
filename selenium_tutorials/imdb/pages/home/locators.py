from selenium.webdriver.common.by import By


class HomePageLocators(object):
    SEARCH_BOX = (By.NAME, 'q')
    SEARCH_BUTTON = (By.ID, 'navbar-submit-button')
