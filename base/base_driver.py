import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def pageScroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(2)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
            if lastCount == pageLength:
                print("true")
                match = True
        time.sleep(3)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_for_presence_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element
