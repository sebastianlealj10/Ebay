import time
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

    def check_size(self):
        element = self.driver.find_element(*SearchPageLocators.SELECT_SIZE_TEN)
        element.click()

    def search_brand(self):
        element = self.driver.find_element(*SearchPageLocators.SELECT_BRAND)
        element.clear()
        element.send_keys("Puma")

    def select_brand_puma(self):
        element = self.driver.find_element(*SearchPageLocators.SELECT_PUMA)
        element.click()

    def results_number(self):
        element = self.driver.find_element(*SearchPageLocators.RESULTS_NUMBER)
        return element.text

    def pick_ten_size_puma(self):
        element = self.driver.find_element(*SearchPageLocators.SELECT_SIZE_TEN)
        element.click()
        element = self.driver.find_element(*SearchPageLocators.SELECT_BRAND)
        element.clear()
        element.send_keys("Puma")
        element = self.driver.find_element(*SearchPageLocators.SELECT_PUMA)
        element.click()

    def sort_items(self):
        time.sleep(5)
        element = self.driver.find_element(*SearchPageLocators.SORT_BUTTON)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        element = self.driver.find_element(*SearchPageLocators.CHECK_LOWEST_FIRST)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.click().perform()
        time.sleep(2)

    def take_products(self, number_of_items):
        element_names = self.driver.find_elements(*SearchPageLocators.ITEMS_NAME)
        element_prices = self.driver.find_elements(*SearchPageLocators.ITEMS_PRICE)
        my_items = build_items_list(self, element_names, element_prices, number_of_items)
        return my_items
