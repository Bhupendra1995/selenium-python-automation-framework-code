import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from utilities.utils import Utils


class SearchFlightResults(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait

    #Locators
    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHTS_RESULTS = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or (contains(text(),'2 Stops'))]"

    def get_filter_flights_by_1_stop_icon(self):
        return self.wait_for_presence_of_element_located(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_flights_by_2_stop_icon(self):
        return self.wait_for_presence_of_element_located(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_flights_by_non_stop_icon(self):
        return self.wait_for_presence_of_element_located(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_all_search_flights_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.SEARCH_FLIGHTS_RESULTS)

    def filter_fLights_by_stops(self,by_stop):
        if by_stop == "1 Stop":
            time.sleep(2)
            self.get_filter_flights_by_1_stop_icon().click()
            self.log.info("selected flights by 1 Stop")
            time.sleep(2)
        elif by_stop == "2 Stop":
            time.sleep(2)
            self.get_filter_flights_by_2_stop_icon().click()
            self.log.info("selected flights by 2 Stop")
            time.sleep(2)
        elif by_stop == "Non Stop":
            time.sleep(2)
            self.get_filter_flights_by_non_stop_icon().click()
            self.log.info("selected flights by Non Stop")
            time.sleep(2)
        else:
            self.log.warning("enter valid stop")



        # time.sleep(2)
        # self.get_filter_flights_by_1_stop_icon().click()
        # time.sleep(2)


    # def filterFlights(self):
    #     time.sleep(2)
    #     #self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='1']"))).click()
    #     self.wait_for_presence_of_element_located(By.XPATH,self.FILTER_BUTTON).click()
    #     time.sleep(2)
