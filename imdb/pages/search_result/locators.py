from selenium.webdriver.common.by import By


class SearchResultPageLocators(object):
    FIND_HEADER = (By.CLASS_NAME, 'findHeader')
    LIST_ITEM = (By.XPATH, '//*[@class="result_text"]/a')
    # LIST_ITEM = (By.CSS_SELECTOR, '.result_text > a')
