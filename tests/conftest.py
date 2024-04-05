import pytest
from selene import browser
from selenium import webdriver
import os

current_file = os.path.abspath(__file__)
components_dir = os.path.dirname(current_file)
root_dir = os.path.dirname(components_dir)
tests_dir = os.path.join(root_dir, 'tests')
resource_dir = os.path.join(tests_dir, 'resource')


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
#    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.window_height = 1920
    browser.config.window_width = 1080

    yield

    browser.quit()
