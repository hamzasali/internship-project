from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given("Open the main page {url}")
def open_main_page(context, url):
    context.driver.get(url)
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#email-2')))


@when("Log in to the page")
def login(context):
    email = context.driver.find_element(By.CSS_SELECTOR, '#email-2')
    email.send_keys('*****')
    password = context.driver.find_element(By.CSS_SELECTOR, "#field[type='password']")
    password.send_keys('*****')
    context.driver.find_element(By.CSS_SELECTOR, "[wized='loginButton']").click()


@when("Click on off plan at the left side menu")
def click_off_plan(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='menu-button'][href*='off-plan']").click()
    sleep(5)


@then("Verify the right page opens")
def verify_right_page(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.url_contains(('off-plan')))
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Total project')]")))
    # context.driver.find_element(By.XPATH, "//div[contains(text(),'Total project')]")


@when("Filter the products by price range from {min} to {max} AED")
def filter_by_price_range(context, min, max):
    context.driver.find_element(By.CSS_SELECTOR, ".filter-button.w-inline-block").click()
    context.driver.find_element(By.CSS_SELECTOR, "[wized='unitPriceFromFilter']").send_keys(min)
    context.driver.find_element(By.CSS_SELECTOR, "[wized='unitPriceToFilter']").send_keys(max)
    context.driver.find_element(By.CSS_SELECTOR, ".button-filter.w-button").click()
    sleep(5)


@then('Verify the price in all cards is inside the range ({min} - {max})')
def verify_price_all_cards(context, min: int, max: int):
    price_list = context.driver.find_elements(By.CSS_SELECTOR, "a[wized='cardOfProperty']  [class='price-value']")
    min = int(min)
    max = int(max)
    for price in price_list:
        price = price.text.split(' ')[1].split(',')
        price = int(''.join(price))

        assert price >= min and price <= max, f'expected price from {min} to {max} but got {price}'
