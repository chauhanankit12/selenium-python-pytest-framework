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
    All_PRODUCTS = (By.XPATH, "//h2[text()='All Products']")
    PRODUCT_LIST = (By.XPATH, "//div[@class='productinfo text-center']")
    FIRST_VIEW_PRODUCT = (By.XPATH, "(//a[@class='btn btn-default add-to-cart'])[1]")
    PRODUCT_NAME = (By.XPATH, "//h2[@class='title text-center']")
    CATEGORY    = (By.XPATH, "//h2[text()='Category']")
    PRICE = (By.XPATH, "//span[@class='product_price']")
    AVAILABLE = (By.XPATH, "//span[@class='product_available']")
    CONDITION = (By.XPATH, "//span[@class='product_condition']")
    BRAND = (By.XPATH, "//span[@class='product_brand']")



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

    def verify_all_products_page(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.All_PRODUCTS)).is_displayed()
            return True
        except Exception as e:
            print(f"Error verifying All Products page: {e}")
            return False

    def verify_products_list(self):

        try:
            product = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_LIST))
            return len(product) > 0
        except Exception as e:
            print(f"Error verifying products list: {e}")
            return False

    def click_first_product(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.FIRST_VIEW_PRODUCT)).click()
        except Exception as e:
            print(f"Error clicking first product: {e}")
            raise

    def verify_product_detail_page(self):
        return "product_details" in self.driver.current_url

    def verify_product_details(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.PRODUCT_NAME)).is_displayed()
            self.wait.until(EC.presence_of_element_located(self.CATEGORY)).is_displayed()
            self.wait.until(EC.presence_of_element_located(self.PRICE)).is_displayed()
            self.wait.until(EC.presence_of_element_located(self.AVAILABLE)).is_displayed()
            self.wait.until(EC.presence_of_element_located(self.CONDITION)).is_displayed()
            self.wait.until(EC.presence_of_element_located(self.BRAND)).is_displayed()
            return True
        except Exception as e:
            print(f"Error verifying product detail page: {e}")
            return False