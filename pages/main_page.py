from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    EMAIL_BOX = (By.ID, 'email-2')

    def open(self):
        self.open_url(f"{self.base_url}/sign-in")
        self.wait_until_clickable(*self.EMAIL_BOX)

    def click_off_plan_from_side(self):
        self.click(By.CSS_SELECTOR, "[class*='menu-button'][href*='off-plan']")
