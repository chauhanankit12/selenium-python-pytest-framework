from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    signup_login = (By.LINK_TEXT, "Signup / Login")


    Proceed_To_Checkout = (By.XPATH, "//a[text()='Proceed To Checkout']")

    Click_Register_Login = (By.XPATH, "//div[@id='checkoutModal']//a[@href='/login']")

    def verify_product_in_cart(self, product_name):
        return len(
            self.driver.find_elements(
                By.XPATH,
                f"//td[@class='cart_description']//a[text()='{product_name}']"
            )
        ) > 0


    def click_proceed_to_checkout(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.Proceed_To_Checkout)).click()
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise


    def click_register_login(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.Click_Register_Login)).click()
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise