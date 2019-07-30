from Locators import SearchPageLocators
from functions import fix_price
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class CheckSize(BasePage):

    def checksize10(self):
        element = self.driver.find_element(*SearchPageLocators.select_size_10)
        element.click()

    def searchbrand(self):
        element = self.driver.find_element(*SearchPageLocators.search_brand)
        element.clear()
        element.send_keys("Puma")

    def selectbrandpuma(self):
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

    def takeproducts(self, number):
        element_names = self.driver.find_elements(*SearchPageLocators.items_name)
        element_prices = self.driver.find_elements(*SearchPageLocators.items_price)
        my_items = []
        for x in range(number):
            price = fix_price(element_prices[x].text)
            my_items.append([element_names[x + 1].text, price])
        return my_items
