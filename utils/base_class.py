# “BaseClass is used to store common methods like driver access, logging, waits,
# and reusable utilities so that all test classes can inherit them and avoid code duplication.”

import pytest
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# This BaseClass will be inherited by all test classes
# It contains reusable utilities like logging and waits
@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        """
        Creates and returns a logger instance
        Each test class will have its own logger
        """
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.INFO)

        # Prevent duplicate logs
        if not logger.handlers:
            ch = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            ch.setFormatter(formatter)
            logger.addHandler(ch)

        return logger

    def wait_for_element(self, locator):
        """
        Explicit wait for element visibility
        locator: tuple (By, value)
        """
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(locator))