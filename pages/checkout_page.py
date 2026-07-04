from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    signup_login = (By.LINK_TEXT, "Signup / Login")
    Delivery_Address = (
        By.XPATH,
        "//h3[contains(text(),'Your delivery address')]"
    )

    Billing_Address = (
        By.XPATH,
        "//h3[contains(text(),'Your billing address')]"
    )

    CLICK_PLACE_ORDER = (By.XPATH, "//a[@href='/payment']")



    def verify_home_page(self):
        try:
            self.wait.until(EC.title_contains("Automation Exercise"))
            return True
        except Exception as e:
            print(f"Error verifying home page: {e}")
            return False

    def verify_delivery_address(self):
        delivery = self.wait.until(
            EC.visibility_of_element_located(self.Delivery_Address)
        )

        billing = self.wait.until(
            EC.visibility_of_element_located(self.Billing_Address)
        )

        return delivery.is_displayed() and billing.is_displayed()

    def verify_order_review(self, product_name):
        return len(
            self.driver.find_elements(
                By.XPATH,
                f"//td[@class='cart_description']//a[text()='{product_name}']"
            )
        ) > 0

    def click_place_order(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CLICK_PLACE_ORDER)).click()
        except Exception as e:
            print(f"Error clicking Place Order: {e}")
            raise