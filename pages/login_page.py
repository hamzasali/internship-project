from selenium.webdriver.common.by import By

from pages.base_page import Page


class LogInPage(Page):
    EMAIL_BOX = (By.ID, 'email-2')
    PASSWORD_BOX = (By.CSS_SELECTOR, "#field[type='password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "[wized='loginButton']")

    def login(self):
        email = self.find_element(*self.EMAIL_BOX)
        email.send_keys('*****') #enter email
        password = self.find_element(*self.PASSWORD_BOX)
        password.send_keys('*****') #enter password
        self.click(*self.LOGIN_BTN)
