from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout, ignored_exceptions=(StaleElementReferenceException,))

    def open(self, url):
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        el = self.wait.until(EC.element_to_be_clickable((by, locator)))
        el.click()
        return el

    def send_keys(self, by, locator, text, clear_first=True):
        el = self.find(by, locator)
        if clear_first:
            el.clear()
        el.send_keys(text)
        return el

    def is_visible(self, by, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located((by, locator))) is not None
        except TimeoutException:
            return False
