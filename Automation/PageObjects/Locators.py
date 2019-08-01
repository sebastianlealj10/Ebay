from selenium.webdriver.common.by import By


class HomePageLocators(object):
    LOGO               = (By.ID, 'gh-logo')
    SEARCH_BAR         = (By.ID, 'gh-ac')
    SEARCH_BUTTON      = (By.ID, 'gh-btn')


class SearchPageLocators(object):
    PRICE_NAV          = (By.ID, 'srp-river-main')
    SELECT_SIZE_TEN    = (By.CSS_SELECTOR, "input[aria-label='10']")
    SELECT_BRAND       = (By.CSS_SELECTOR, ".x-searchable-list__textbox__aspect-Brand")
    SELECT_PUMA        = (By.CSS_SELECTOR, "input[aria-label='PUMA']")
    RESULTS_NUMBER     = (By.CSS_SELECTOR, ".srp-controls__count-heading")
    SORT_BUTTON        = (By.CSS_SELECTOR, "button[aria-controls='w7']")
    SORT_NEWLY         = (By.CSS_SELECTOR, "ul[class='srp-sort__menu'] > li:nth-child(2)")
    CHECK_LOWEST_FIRST = (By.CSS_SELECTOR, "ul[class='srp-sort__menu'] > li:nth-child(4)")
    ITEMS_NAME         = (By.CSS_SELECTOR, ".s-item__title")
    ITEMS_PRICE        = (By.CSS_SELECTOR, ".s-item__price")
