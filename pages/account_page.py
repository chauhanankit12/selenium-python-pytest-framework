from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    account_info = (By.XPATH, "//b[text()='Enter Account Information']")
    title_mr = (By.ID, "id_gender1")
    password = (By.ID, "password")

    days = (By.ID, "days")
    months = (By.ID, "months")
    years = (By.ID, "years")

    newsletter = (By.ID, "newsletter")
    offers = (By.ID, "optin")

    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    address = (By.ID, "address1")
    country = (By.ID, "country")
    state = (By.ID, "state")
    city = (By.ID, "city")
    zipcode = (By.ID, "zipcode")
    mobile = (By.ID, "mobile_number")

    create_account = (By.XPATH, "//button[text()='Create Account']")
    account_created = (By.XPATH, "//b[text()='Account Created!']")
    continue_btn = (By.XPATH, "//a[text()='Continue']")
    delete_account = (By.XPATH, "//a[normalize-space()='Delete Account']")
    account_deleted = (By.XPATH, "//b[normalize-space()='Account Deleted!']")

    logged_in_user = (By.XPATH, "//a[contains(text(),'Logged in as')]")



    def fill_account_info(self):
        """
        Fill basic account details like title, password, DOB
        """
        self.driver.find_element(*self.title_mr).click()
        self.driver.find_element(*self.password).send_keys("Test@123")

        # Handle dropdowns using Select class
        Select(self.driver.find_element(*self.days)).select_by_value("10")
        Select(self.driver.find_element(*self.months)).select_by_visible_text("May")
        Select(self.driver.find_element(*self.years)).select_by_value("1995")

        # Select checkboxes
        self.driver.find_element(*self.newsletter).click()
        self.driver.find_element(*self.offers).click()

    def fill_address(self):
        """
        Fill address and contact details
        """
        self.driver.find_element(*self.first_name).send_keys("John")
        self.driver.find_element(*self.last_name).send_keys("Doe")
        self.driver.find_element(*self.address).send_keys("India")

        # Country dropdown
        Select(self.driver.find_element(*self.country)).select_by_visible_text("India")

        self.driver.find_element(*self.state).send_keys("UP")
        self.driver.find_element(*self.city).send_keys("Moradabad")
        self.driver.find_element(*self.zipcode).send_keys("244001")
        self.driver.find_element(*self.mobile).send_keys("9999999999")

    def create_account_btn(self):
        """Click on Create Account button"""
        self.driver.find_element(*self.create_account).click()

    def verify_account_created(self):
        """Verify account creation success message"""
        return self.driver.find_element(*self.account_created).is_displayed()

    def click_continue(self):
        """Click Continue button"""
        self.driver.find_element(*self.continue_btn).click()

    def verify_logged_in(self):
        """Verify user is logged in"""
        return self.driver.find_element(*self.logged_in_user).is_displayed()

    def delete_account_btn(self):
        """Click Delete Account button"""
        self.driver.find_element(*self.delete_account).click()

    def verify_account_deleted(self):
        """Verify account deletion message"""
        return self.driver.find_element(*self.account_deleted).is_displayed()