import unittest
import time
import sys

sys.path.extend(['/home/sebas/PycharmProjects/Ebay', '/home/sebas/PycharmProjects/Ebay/Automation', '/home/sebas'
                                                                                                    '/PycharmProjects'
                                                                                                    '/Ebay/Automation'
                                                                                                    '/PageObjects',
                 '/home/sebas/PycharmProjects/Ebay/Automation/Scripts',
                 '/home/sebas/PycharmProjects/Ebay/Automation/PageObjects/Pages',
                 '/home/sebas/PycharmProjects/Ebay/venv', '/home/sebas/PycharmProjects/Ebay/venv/bin',
                 '/home/sebas/PycharmProjects/Ebay/venv/include', '/home/sebas/PycharmProjects/Ebay/venv/lib',
                 '/home/sebas/PycharmProjects/Ebay/venv/lib64'])

from selenium import webdriver
from Pages import Homepage
from Pages import Searchpage
from functions import sort_by_price_asc
from functions import sort_by_price_desc
from functions import sort_by_name_desc

import sys;

print('Python %s on %s' % (sys.version, sys.platform))


class SearchShoes(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://www.ebay.com/")

    def test_order_shoes(self):
        number_of_items = 5
        home_page = Homepage.SearchTab(self.driver)
        home_page.writeOnSeachbar()
        home_page.search()
        search_page = Searchpage.CheckSize(self.driver)
        search_page.searchbrand()
        search_page.checksize10()
        time.sleep(5)
        search_page.selectbrandpuma()
        results = search_page.resultsnumber()
        print("Total resuts for the search: " + str(results))
        search_page.sortitems()
        time.sleep(5)
        items = search_page.takeproducts(number_of_items)
        print("First 5 items found: " + str(items))
        print("Items sorted by name ASC" + str(sort_by_price_desc(items)))
        print("Items sorted by price DESC" + str(sort_by_name_desc(items)))
        self.assertListEqual(items, sort_by_price_asc(items),
                             msg="Items are not sorted correctly")

    def tearDown(self):
        # close the browser window
        self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(SearchShoes('test_order_shoes'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
