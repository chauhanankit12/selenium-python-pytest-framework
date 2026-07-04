import pytest
import random
import string
from utils.base_class import BaseClass
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


# logger = BaseClass.get_logger()


class TestVerifyProductDetailsPage(BaseClass):

    def generate_email(self):
        random_str = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"test_{random_str}@mail.com"

    def test_Verify_Product_Details_page(self):
        """
        Test Case 14:
        Place Order - Register While Checkout
        """

        log = self.get_logger()

        home = HomePage(self.driver)
        products = ProductsPage(self.driver)
        cart = CartPage(self.driver)


        try:
            # Verify Home Page
            log.info("Verifying home page")
            assert home.verify_home_page()

            log.info("Clicking Products")
            home.click_products()

            log.info("Verifying All Products page")
            assert products.verify_all_products_page()

            log.info("Verifying Products List")
            assert products.verify_products_list()

            log.info("Opening First Product")
            products.click_first_product()

            log.info("Verifying Product Detail Page")
            assert products.verify_product_detail_page()

            log.info("Verifying Product Information")
            assert products.verify_product_details()

            log.info("Product details verified successfully")

        except Exception as e:
            log.error(f"Place Order Register While Checkout Test Failed: {str(e)}")
            raise

        finally:
            print("Place Order Register While Checkout Test Completed")