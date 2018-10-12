from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverWaits(object):

    def __init__(self, driver, timeout=30, poll_frequency=0.5):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)

    def wait_till_element_visible(self, locator, message=None):
        if not message:
            message = 'Element not visible in time'
        self.wait.until(EC.visibility_of_element_located(locator), message)

    # def wait_till_url_is_changed(self):
    #     self.wait.until(EC, )