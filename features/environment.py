from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application
from support.logger import logger


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    #           chrome
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=Options())

    #           mobile testing
    # mobile_emulation = {"deviceName": "iPad Mini"}
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 600, "height": 1024, "pixelRatio": 2.0},
    #     "userAgent": "Mozilla/5.0 (iPad; CPU OS 13_0 like Mac OS X) "
    #                  "AppleWebKit/605.1.15 (KHTML, like Gecko) "
    #                  "Version/13.0 Mobile/15E148 Safari/604.1"
    # }
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(options=chrome_options)

    #           firefox
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    #           safari
    # context.driver = webdriver.Safari()

    #           headless
    # option = (webdriver.ChromeOptions())
    # option.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=option)

    #       browser stack
    bs_user = '*****' #enter your username and password
    bs_key = '*****'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    # bstack_options = {
    #     "os": "Windows",
    #     "osVersion": "11",
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name,
    #
    # }
    bstack_options = {
        'deviceName': 'Samsung Galaxy S20 Ultra',
        'osVersion': '13.0',
        'browserName': 'samsung',
        'deviceOrientation': 'portrait',
        'sessionName': scenario_name,
    }
    # bstack_options = {
    #     'deviceName': 'iPhone 12 Pro',
    #     'osVersion': 18,
    #     'browserName': 'chromium',
    #     'deviceOrientation': 'portrait',
    #     'sessionName': scenario_name,
    # }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
