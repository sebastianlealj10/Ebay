from Locators import SearchPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from functions import build_items_list


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class SortItems(BasePage):

    def check_page_loaded(self):
        return True if self.driver.find_element(*SearchPageLocators.PRICE_NAV) else False

    def checksize(self):
        element = self.driver.find_element(*SearchPageLocators.select_size_10)
        element.click()

    def searchbrand(self):
        element = self.driver.find_element(*SearchPageLocators.search_brand)
        element.clear()
        element.send_keys("Puma")

    def selectbrandpuma(self):
        element = self.driver.find_element(*SearchPageLocators.select_puma)
        element.click()

    def pick_ten_size_puma(self):
        element = self.driver.find_element(*SearchPageLocators.select_size_10)
        element.click()
        element = self.driver.find_element(*SearchPageLocators.search_brand)
        element.clear()
        element.send_keys("Puma")
        element = self.driver.find_element(*SearchPageLocators.select_puma)
        element.click()

    def resultsnumber(self):
        element = self.driver.find_element(*SearchPageLocators.results_number)
        return element.text

    def sortitems(self):
        element = self.driver.find_element(*SearchPageLocators.sort_button)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        element = self.driver.find_element(*SearchPageLocators.check_lowest_first)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.click().perform()

    def takeproducts(self, numberofitems):
        element_names = self.driver.find_elements(*SearchPageLocators.items_name)
        element_prices = self.driver.find_elements(*SearchPageLocators.items_price)
        my_items = build_items_list(self, element_names, element_prices, numberofitems)
        return my_items
