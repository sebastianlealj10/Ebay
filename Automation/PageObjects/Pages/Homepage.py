from Locators import HomePageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class SearchTab(BasePage):

    def check_page_loaded(self):
        return True if self.driver.find_element(*HomePageLocators.LOGO) else False

    def search_bar_text(self):
        element = self.driver.find_element(*HomePageLocators.SEARCH_BAR)
        element.clear()
        element.send_keys("Shoes")

    def search_button(self):
        element = self.driver.find_element(*HomePageLocators.SEARCH_BUTTON)
        element.click()

    def search_shoes(self):
        self.search_bar_text()
        self.search_button()


