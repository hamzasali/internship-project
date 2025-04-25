from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    EMAIL_BOX = (By.ID, 'email-2')
    OFF_PLAN_SIDE_BTN = (By.CSS_SELECTOR, "[class*='menu-button'][href*='off-plan']")

    def open(self):
        self.open_url(f"{self.base_url}/sign-in")
        self.wait_until_clickable(*self.EMAIL_BOX)

    def click_off_plan_from_side(self):
        self.click(*self.OFF_PLAN_SIDE_BTN)
        sleep(2)
