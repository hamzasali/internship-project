from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class OffPlanPage(Page):
    OFF_PLAN_TXT = (By.XPATH, "//a[contains(text(),'Off-plan')]")
    TOTAL_TXT = (By.XPATH, "//div[contains(text(),'Total project')]")
    FILTER_BTN = (By.CSS_SELECTOR, ".filter-button.w-inline-block")
    FILTER_BTN_MOBILE = (By.CSS_SELECTOR, ".filter-button")
    MIN_BOX = (By.CSS_SELECTOR, "[wized='unitPriceFromFilter']")
    MAX_BOX = (By.CSS_SELECTOR, "[wized='unitPriceToFilter']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "[wized='applyFilterButton']")
    PRICE_LST = (By.CSS_SELECTOR, "a[wized='cardOfProperty']  [class='price-value']")

    def verify_right_page(self):
        self.verify_partial_url('off-plan')
        self.wait_until_visible(*self.OFF_PLAN_TXT)
        self.wait_until_visible(*self.TOTAL_TXT)

    def filter_by_price_range(self, min, max):
        self.wait_until_clickable_click(*self.FILTER_BTN)  # web testing
        self.input_text(min, *self.MIN_BOX)
        self.input_text(max, *self.MAX_BOX)
        self.click(*self.APPLY_FILTER_BTN)
        sleep(4)

    def filter_by_price_range_mobile(self, min, max):
        self.wait_until_clickable_click(*self.FILTER_BTN_MOBILE)  # mobile testing
        self.input_text(min, *self.MIN_BOX)
        self.input_text(max, *self.MAX_BOX)
        self.click(*self.APPLY_FILTER_BTN)
        sleep(4)

    def verify_prices_all_cards(self, min, max):
        price_list = self.find_elements(*self.PRICE_LST)
        min = int(min)
        max = int(max)
        for price in price_list:
            price = price.text.split(' ')[1].split(',')
            price = int(''.join(price))

            assert price >= min and price <= max, f'expected price from {min} to {max} but got {price}'
