# Share fixtures, hooks, and setup/teardown logic across multiple test files.

import logging

import pytest
import selenium

from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    logging.info("Setting up Chrome driver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    # Open application URL
    driver.get("https://automationexercise.com/")
    logging.info("Application opened")

    # Attach driver to class
    request.cls.driver = driver

    yield

    logging.info("Closing browser")
    driver.quit()



