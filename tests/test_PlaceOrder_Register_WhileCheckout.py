import pytest
import random
import string
from utils.base_class import BaseClass
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.signup_login_page import SignupLoginPage
from pages.account_page import AccountPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage

# logger = BaseClass.get_logger()


class TestPlaceOrderRegisterWhileCheckout(BaseClass):

    def generate_email(self):
        random_str = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"test_{random_str}@mail.com"

    def test_place_order_register_while_checkout(self):
        """
        Test Case 14:
        Place Order - Register While Checkout
        """

        log = self.get_logger()

        home = HomePage(self.driver)
        products = ProductsPage(self.driver)
        cart = CartPage(self.driver)
        signup = SignupLoginPage(self.driver)
        account = AccountPage(self.driver)
        checkout = CheckoutPage(self.driver)
        payment = PaymentPage(self.driver)

        try:
            # Verify Home Page
            log.info("Verifying home page")
            assert home.verify_home_page()

            # Add products to cart
            log.info("Adding products to cart")
            products.add_product_to_cart()
            products.continue_shopping()
            products.add_second_product_to_cart()
            products.view_cart()

            # Verify Cart Page
            log.info("Verifying cart page")
            assert cart.verify_product_in_cart("Sleeveless Dress")
            assert cart.verify_product_in_cart("Summer White Top")

            # Proceed To Checkout
            log.info("Proceeding to checkout")
            cart.click_proceed_to_checkout()

            # Register/Login
            log.info("Opening Signup/Login page")
            cart.click_register_login()

            # Register New User
            email = self.generate_email()

            log.info(f"Registering user with email: {email}")

            signup.enter_name_email("Test User", email)
            signup.click_signup()

            self.wait_for_element(account.account_info)

            account.fill_account_info()
            account.fill_address()
            account.create_account_btn()

            # Verify Account Created
            log.info("Verifying account creation")
            assert account.verify_account_created()

            account.click_continue()

            # Verify Logged In
            log.info("Verifying logged in user")
            assert account.verify_logged_in()

            # Navigate Back To Cart
            log.info("Opening cart again")
            home.click_cart()

            cart.click_proceed_to_checkout()

            # Verify Address Details
            log.info("Verifying address details")
            assert checkout.verify_delivery_address()

            # Verify Review Order
            log.info("Verifying order review section")
            assert checkout.verify_order_review()

            # Enter Comment
            logger.info("Entering order comment")
            checkout.enter_comment(
                "Automation Order Testing"
            )

            # Place Order
            log.info("Clicking Place Order")
            checkout.click_place_order()

            # Payment Information
            log.info("Entering payment details")
            payment.enter_name_on_card("Test User")
            payment.enter_card_number("4111111111111111")
            payment.enter_cvc("123")
            payment.enter_expiry_month("12")
            payment.enter_expiry_year("2030")

            payment.click_pay_and_confirm()

            # Verify Success Message
            log.info("Verifying order success message")
            success_message = payment.get_success_message()

            assert "Your order has been placed successfully!" in success_message

            log.info("Order placed successfully")

            # Delete Account
            log.info("Deleting account")
            account.delete_account_btn()

            assert account.verify_account_deleted()

            log.info("Account deleted successfully")

        except Exception as e:
            log.error(f"Place Order Register While Checkout Test Failed: {str(e)}")
            raise

        finally:
            print("Place Order Register While Checkout Test Completed")