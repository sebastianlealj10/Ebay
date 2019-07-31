import unittest
import time
import sys
import os
from pathlib import Path

dir_path = os.path.abspath(__file__ + "/../../..")
print(dir_path)

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([dir_path,
                 dir_path + '/Automation',
                 dir_path + '/Automation''/PageObjects',
                 dir_path + '/Automation''/drivers',
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
                 dir_path + '/venv/lib/python3.7/site-packages/config-0.4.2-py3.7.egg-info',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/EGG-INFO',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7'
                            '.egg/pip/_internal/cli',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/commands',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_internal/models',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/operations',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0'
                            '.3-py3.7.egg/pip/_internal/req',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/utils',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_internal/vcs',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/cachecontrol',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/cachecontrol/caches',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0'
                            '.3-py3.7.egg/pip/_vendor/certifi',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/chardet',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
                            '/pip/_vendor/chardet/cli',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/colorama',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
                            '/pip/_vendor/distlib',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/distlib/_backport',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/html5lib',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/html5lib/_trie',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3'
                            '.7.egg/pip/_vendor/html5lib/filters',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/html5lib/treeadapters',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/html5lib/treebuilders',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/html5lib/treewalkers',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0'
                            '.3-py3.7.egg/pip/_vendor/idna',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/lockfile',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
                            '/pip/_vendor/msgpack',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/packaging',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7'
                            '.egg/pip/_vendor/pep517',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/pkg_resources',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3'
                            '.7.egg/pip/_vendor/progress',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/pytoml',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
                            '/pip/_vendor/requests',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/urllib3',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
                            '/pip/_vendor/urllib3/contrib',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/urllib3/contrib/_securetransport',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/urllib3/packages',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/urllib3/packages/backports',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/urllib3/packages/ssl_match_hostname',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/urllib3/util',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7'
                            '.egg/pip/_vendor/webencodings',
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
                            '', dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/firefox'
                                           '/x86',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/ie'
                            '',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium'
                            '/webdriver/opera',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/phantomjs',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/remote',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/safari',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/support',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/webkitgtk',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium-3.141.0.dist-info',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/contrib',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/contrib/_securetransport'
                            '',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/packages',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/packages/backports',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/packages/rfc3986',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/packages'
                            '/ssl_match_hostname',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3'
                            '/util',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3-1.25.3.dist-info',
                 dir_path + '/venv/lib64/python3.7',
                 dir_path + '/venv/lib64/python3.7/site-packages',
                 dir_path + '/venv/lib64/python3.7/site-packages/config-0.4.2-py3.7.egg-info',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/EGG-INFO',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7'
                            '.egg/pip/_internal/cli',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/commands',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0'
                            '.3-py3.7.egg/pip/_internal/models',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/operations',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19'
                            '.0.3-py3.7.egg/pip/_internal/req',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/utils',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_internal/vcs',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7'
                            '.egg/pip/_vendor/cachecontrol',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/cachecontrol/caches',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/certifi',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/chardet',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/chardet/cli',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19'
                            '.0.3-py3.7.egg/pip/_vendor/colorama',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/distlib',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/distlib/_backport',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/html5lib',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/html5lib/_trie',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/html5lib/filters',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/html5lib/treeadapters',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/html5lib/treebuilders',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/html5lib/treewalkers',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/idna',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3'
                            '.7.egg/pip/_vendor/lockfile',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/msgpack',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/packaging',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/pep517',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/pkg_resources',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/progress',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/pytoml',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/requests',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/urllib3',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/contrib',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/contrib/_securetransport',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/packages',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/packages/backports',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/packages/ssl_match_hostname',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/util',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19'
                            '.0.3-py3.7.egg/pip/_vendor/webencodings',
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
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium-3.141.0.dist-info',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3/contrib'
                            '/_securetransport',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3'
                            '/contrib',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3/packages',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3/packages/backports',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3/packages/rfc3986',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3/packages'
                            '/ssl_match_hostname',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3'
                            '/util',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3-1.25.3.dist-info'])

from selenium import webdriver
from Pages import Homepage
from Pages import Searchpage
from functions import sort_by_price_asc
from functions import sort_by_price_desc
from functions import sort_by_name_asc
from functions import print_results


class SearchShoes(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox(Path(dir_path + '/Automation/drivers'))
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://www.ebay.com/")

    def test_order_shoes(self):
        number_of_items = 5
        home_page = Homepage.SearchTab(self.driver)
        home_page.writeOnSeachbar()
        home_page.search()
        search_page = Searchpage.SortItems(self.driver)
        search_page.searchbrand()
        search_page.checksize()
        time.sleep(5)
        search_page.selectbrandpuma()
        results = search_page.resultsnumber()
        print("Total resuts for the search: " + str(results))
        print("........................................................................................\n")
        search_page.sortitems()
        time.sleep(5)
        items = search_page.takeproducts(number_of_items)
        print_results(items, "First five results")
        print_results(sort_by_name_asc(items), "Items sorted by name ASC")
        print_results(sort_by_price_desc(items), "Items sorted by price DESC")
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
