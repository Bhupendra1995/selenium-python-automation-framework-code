import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.search_flights_result_page import SearchFlightResults


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    # Locators
    DEPART_FROM_LOCATION = "//input[@id='BE_flight_origin_city']"
    ALL_DEPART_LOCATION = "//div[@class='viewport']//li"
    GOING_TO_LOCATION = "//input[@id='BE_flight_arrival_city']"
    ALL_GOING_LOCATION = "//div[@class='viewport']//div[1]//li"
    DEPART_DATE = "//input[@id='BE_flight_origin_date']"
    ALL_DEPART_DATE = '//div[@id="monthWrapper"]//tbody//td[@class!="inActiveTD" and @class!="weekend" and @class!="inActiveTD weekend"]'
    CLICK_SEARCH_BUTTON = "//input[@value='Search Flights']"
    def getDepartFromField(self):
        return self.wait_for_presence_of_element_located(By.XPATH, self.DEPART_FROM_LOCATION)

    def getAllDepartLocation(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.ALL_DEPART_LOCATION)

    def getGoingToLocation(self):
        return self.wait_for_presence_of_element_located(By.XPATH, self.GOING_TO_LOCATION)

    def getAllGoingToLocation(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ALL_GOING_LOCATION)

    def getDepartDate(self):
        return self.wait_for_presence_of_element_located(By.XPATH, self.DEPART_DATE)

    def getAllDepartDate(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.ALL_DEPART_DATE)

    def getClickSearchButton(self):
        return self.wait_for_presence_of_element_located(By.XPATH, self.CLICK_SEARCH_BUTTON)

    def enterDepartFromLocation(self,departLocation):
        depart_from = self.getDepartFromField()
        time.sleep(2)
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys(departLocation)
        time.sleep(2)
        all_depart = self.getAllDepartLocation()
        all_depart[0].click()
        # for ele in all_depart:
        #     if "London (LON)" in ele.text:
        #         ele.click()
        #         break


    def enterGoingToLocation(self,goingtoLocation):
        going_to = self.getGoingToLocation()
        going_to.click()
        time.sleep(2)
        going_to.send_keys(goingtoLocation)
        time.sleep(2)
        result2 = self.getAllGoingToLocation()
        result2[0].click()
        # for res in result2:
        #     if "Agra" in res.text:
        #         res.click()
        #         break

    def enterDepartDate(self,departureDate):
        depart_date = self.getDepartDate()
        depart_date.click()
        all_dates = self.getAllDepartDate()

        for date in all_dates:
            if (date.get_attribute("data-date") == departureDate):
                date.click()
                break

    def enterClickSearch(self):
        self.getClickSearchButton().click()
        time.sleep(2)

    def search_flights_main(self, departLocation, goingtoLocation, departureDate):
        self.enterDepartFromLocation(departLocation)
        self.enterGoingToLocation(goingtoLocation)
        self.enterDepartDate(departureDate)
        self.enterClickSearch()
        search_flight_res = SearchFlightResults(self.driver)
        return search_flight_res

    # def DepartFrom(self, departLocation):
    #     depart_form = self.wait_for_presence_of_element_located(By.XPATH, self.DEPART_FROM_LOCATION)
    #     depart_form.click()
    #     time.sleep(3)
    #     depart_form.send_keys(departLocation)
    #     time.sleep(2)
    #     all_depart = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']//li")
    #     all_depart[0].click()
    #     # for ele in all_depart:
    #     #     if "London (LON)" in ele.text:
    #     #         ele.click()
    #     #         break

    # def goingTo(self,goingtoLocation):
    #     going_to = self.wait_for_presence_of_element_located(By.XPATH, self.GOING_TO_LOCATION)
    #     going_to.click()
    #     time.sleep(2)
    #     going_to.send_keys(goingtoLocation)
    #     time.sleep(2)
    #     result2 = self.wait_for_presence_of_all_elements(By.XPATH, self.ALL_GOING_LOCATION)
    #     result2[0].click()
    #     # for res in result2:
    #     #     if "Agra" in res.text:
    #     #         res.click()
    #     #         break

    # def DepartDate(self,departureDate):
    #     depart_date = self.wait_for_presence_of_element_located(By.XPATH, self.DEPART_DATE)
    #     depart_date.click()
    #     all_dates = self.wait_for_presence_of_all_elements(By.XPATH,self.ALL_DEPART_DATE)
    #
    #     for date in all_dates:
    #         if (date.get_attribute("data-date") == departureDate):
    #             date.click()
    #             break

    # def clickSearch(self):
    #     #     self.wait_for_presence_of_element_located(By.XPATH, self.CLICK_SEARCH_BUTTON).click()
    #     #     time.sleep(2)