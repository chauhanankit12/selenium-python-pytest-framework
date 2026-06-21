import pytest
import random
import string
from utils.base_class import  BaseClass
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_page import AccountPage


class TestRegisterUser(BaseClass):


    def generate_email(self):
        """
        Generate random email to avoid duplicate user issue
        """
        random_str = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"test_{random_str}@mail.com"

    def test_register_user(self):
        """
        End-to-End Test Case:
        Register -> Login -> Delete Account
        """
        log = self.get_logger()
        home = HomePage(self.driver)
        signup = SignupLoginPage(self.driver)
        account = AccountPage(self.driver)
        try:
            # Step 1: Verify home page

            assert home.verify_home_page()
            log.info("Home page verified")

            # Step 2: Navigate to Signup/Login page
            home.click_signup_login()

            # Step 3: Verify Signup section

            assert signup.verify_new_user()
            log.info("Signup page verified")

            # Step 4: Enter name and random email
            email = self.generate_email()
            signup.enter_name_email("TestUser", email)
            signup.click_signup()



            # Step 5: Wait for account info page (Explicit wait)
            self.wait_for_element(account.account_info)

            # Step 6: Fill account details
            account.fill_account_info()
            account.fill_address()
            account.create_account_btn()

            # Step 7: Verify account created
            assert account.verify_account_created()
            log.info("Account created successfully")

            # Step 8: Click Continue
            account.click_continue()

            # Step 9: Verify user logged in
            self.wait_for_element(account.logged_in_user)
            assert account.verify_logged_in()
            log.info("User logged in successfully")

            # Step 10: Delete account
            account.delete_account_btn()

            # Step 11: Verify account deleted
            self.wait_for_element(account.account_deleted)
            assert account.verify_account_deleted()
            log.info("Account Deleted!")

        except Exception as e:
            log.error(f"Register User Test failed: {e}")
            raise


