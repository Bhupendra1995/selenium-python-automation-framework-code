import time
import pytest
import softest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt, data, unpack, file_data


@pytest.mark.usefixtures("setUp")
@ddt()
class TestSearchAndFlights(softest.TestCase):

    log = Utils.custom_logger()
    ut = Utils()
    #depart_date = ut.find_Date()

    @pytest.fixture(autouse=True)
    def class_obj_setup(self):
        self.lp = LaunchPage(self.driver)

    # this provides the link of this driver to the test case with the help of request
    # @data(("London", "Mum", depart_date, "1 Stop"), ("Mum", "JFK", depart_date, "2 Stop"))
    # @unpack
    # @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testyml.yaml")
    # @data(*Utils.read_data_from_excel("C:\\Python Selenium\\TestAutomationFramework\\testdata\\tdataexcel.xlsx", "Sheet1"))
    @data(*Utils.read_data_from_csv("C:\\Python Selenium\\TestAutomationFramework\\testdata\\testcsv.csv"))
    @unpack
    def test_search_flights_1_stop(self, going_from, going_to, d_date, stop):
        # Flight search main method
        search_flight_res = self.lp.search_flights_main(going_from, going_to, d_date)

        # handling of page scroll with javascript
        self.lp.pageScroll()

        # click on the Filter type
        search_flight_res.filter_fLights_by_stops(stop)

        # Find out all the search flights
        all_stops = search_flight_res.get_all_search_flights_results()
        self.log.info(len(all_stops))

        # verify the filter showing only 1 stops
        self.ut.assertListItemText(all_stops, stop)
        time.sleep(3)


        # providing going from location
        # lp.enterDepartFromLocation("London")

        # providing going to location
        # lp.enterGoingToLocation("new")

        # Select the departure date
        # lp.enterDepartDate(depart_date)

        # click on flight search button
        # lp.enterClickSearch()

        # sf = SearchFlightResults(self.driver)

        # all_stops = sf.wait_for_presence_of_all_elements(By.XPATH,"//span[contains(text()
        # ,'Non Stop') or contains(text(),'1 Stop') or (contains(text(),'2 Stops'))]")
