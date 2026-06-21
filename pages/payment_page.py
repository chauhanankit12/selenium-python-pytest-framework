from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    signup_login = (By.LINK_TEXT, "Signup / Login")



    def verify_home_page(self):
        try:
            self.wait.until(EC.title_contains("Automation Exercise"))
            return True
        except Exception as e:
            print(f"Error verifying home page: {e}")
            return False