import unittest
import time
import sys
import os

dir_path = os.path.abspath(__file__ + "/../../..")
sys.path.extend([dir_path,
                 dir_path + '/Automation',
                 dir_path + '/Automation/PageObjects',
                 dir_path + '/Automation/drivers',
                 dir_path + '/Automation/Scripts',
                 dir_path + '/Automation/PageObjects/Pages',
                 dir_path + '/venv',
                 dir_path + '/venv/bin',
                 dir_path + '/venv/include',
                 dir_path + '/venv/lib',
                 dir_path + '/venv/lib64',
                 dir_path + '/.idea',
                 dir_path + '/.idea/inspectionProfiles',
                 dir_path + '/venv/lib/python3.7',
                 dir_path + '/venv/lib/python3.7/site-packages',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/common',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/android',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/blackberry',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/chrome',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/common',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/common/actions'
                            '',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/common'
                            '/html5',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver'
                            '/edge',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium'
                            '/webdriver/firefox',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/firefox/amd64'
                            '',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/firefox/x86',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/ie',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium'
                            '/webdriver/opera',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/phantomjs',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/remote',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/safari',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/support',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/webkitgtk',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium-3.141.0.dist-info',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/common',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/android',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/blackberry',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/common',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/chrome',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/common'
                            '/actions',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver'
                            '/common/html5',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/edge',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/firefox',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/firefox'
                            '/amd64',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver'
                            '/firefox/x86',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/ie',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/opera',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/phantomjs',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/remote',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/safari',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/support',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/webkitgtk',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium-3.141.0.dist-info'])

from selenium import webdriver
from functions import *
from Homepage import SearchTab
from Searchpage import SortItems


class TestSearchShoes(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.ebay.com/")

    def test_home_page_load(self):
        home_page = SearchTab(self.driver)
        self.assertTrue(home_page.check_page_loaded())

    def test_home_search(self):
        home_page = SearchTab(self.driver)
        home_page.search_shoes()

    def test_search_page_load(self):
        home_page = SearchTab(self.driver)
        home_page.search_shoes()
        search_page = SortItems(self.driver)
        self.assertTrue(search_page.check_page_loaded())

    def test_pick_brand_and_size(self):
        home_page = SearchTab(self.driver)
        home_page.search_shoes()
        search_page = SortItems(self.driver)
        search_page.pick_ten_size_puma()
        results = search_page.results_number()
        time.sleep(2)
        print("Total resuts for the search: " + str(results))
        print("........................................................................................\n")

    def test_sort_items_asc(self):
        number_of_items = 5
        home_page = SearchTab(self.driver)
        time.sleep(5)
        home_page.search_shoes()
        search_page = SortItems(self.driver)
        search_page.pick_ten_size_puma()
        search_page.sort_items()

        items = search_page.take_products(number_of_items)
        print_results(items, "First five results")
        print_results(sort_by_name_asc(items), "Items sorted by name ASC")
        print_results(sort_by_price_desc(items), "Items sorted by price DESC")
        self.assertListEqual(items, sort_by_price_asc(items),
                             msg="Items are not sorted correctly")

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchShoes)
    suite = unittest.TestSuite()
    suite.addTest(TestSearchShoes('test_sort_items_asc'))
    unittest.TextTestRunner(verbosity=2).run(suite)
