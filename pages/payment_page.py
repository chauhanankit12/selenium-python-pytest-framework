from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    ENTER_NAME_ON_CARD = (By.NAME, "name_on_card")
    ENTER_CARD_NUMBER = (By.NAME, "card_number")
    ENTER_CVC = (By.NAME, "cvc")
    ENTER_EXPIRY_MONTH = (By.NAME, "expiry_month")
    ENTER_EXPIRY_YEAR = (By.NAME, "expiry_year")
    CLICK_ON_PAY_AND_CONFIRM_ORDER = (By.ID, "submit")
    success_message = (By.XPATH, "//p[text()='Congratulations! Your order has been confirmed!']")



    def enter_name_on_card(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.ENTER_NAME_ON_CARD)).send_keys("Test User")
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise

    def enter_card_number(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.ENTER_CARD_NUMBER)).send_keys("4111111111111111")
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise

    def enter_cvc(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.ENTER_CVC)).send_keys("123")
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise

    def enter_expiry_month(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.ENTER_EXPIRY_MONTH)).send_keys("12")
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise

    def enter_expiry_year(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.ENTER_EXPIRY_YEAR)).send_keys("2030")
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise

    def click_on_pay_and_confirm_order(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CLICK_ON_PAY_AND_CONFIRM_ORDER)).click()
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_message)
        ).text