from Locators import HomePageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class SearchTab(BasePage):

    def writeOnSeachbar(self):
        element = self.driver.find_element(*HomePageLocators.search_bar)
        element.clear()
        element.send_keys("Shoes")

    def search(self):
        element = self.driver.find_element(*HomePageLocators.search_button)
        element.click()
