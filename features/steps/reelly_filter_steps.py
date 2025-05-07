from behave import given, when, then


@given("Open the main page")
def open_main_page(context):
    context.app.main_page.open()


@when("Log in to the page")
def login(context):
    context.app.login_page.login()


@when("Click on off plan at the left side menu")
def click_off_plan(context):
    context.app.main_page.click_off_plan_from_side()


@when("Click on off plan slide on mobile")
def click_off_plan(context):
    context.app.main_page.click_off_plan_slide()


@then("Verify the right page opens")
def verify_right_page(context):
    context.app.off_plan_page.verify_right_page()


@when("Filter the products by price range from {min} to {max} AED")
def filter_by_price_range(context, min, max):
    context.app.off_plan_page.filter_by_price_range(min, max)


@when("Filter the products by price range from {min} to {max} AED mobile")
def filter_by_price_range(context, min, max):
    context.app.off_plan_page.filter_by_price_range_mobile(min, max)


@then('Verify the price in all cards is inside the range ({min} - {max})')
def verify_price_all_cards(context, min: int, max: int):
    context.app.off_plan_page.verify_prices_all_cards(min, max)
