from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    Add_Product_To_Cart = (By.XPATH, "//a[@data-product-id='3']")
    Continue_Shopping = (By.XPATH, "//button[text()='Continue Shopping']")
    View_Cart = (By.XPATH, "//a[@href='/view_cart']")
    Add_Second_Product_To_Cart = (By.XPATH, "//a[@data-product-id='6']")



    def add_product_to_cart(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.Add_Product_To_Cart)).click()
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise


    def continue_shopping(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.Continue_Shopping)).click()
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise


    def view_cart(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.View_Cart)).click()
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise

    def add_second_product_to_cart(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.Add_Second_Product_To_Cart)).click()
        except Exception as e:
            print(f"Error clicking Signup/Login: {e}")
            raise