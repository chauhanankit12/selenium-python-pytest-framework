from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SignupLoginPage:


    new_user_text = (By.XPATH, "//h2[text()='New User Signup!']")
    name = (By.NAME, "name")
    email = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_btn = (By.XPATH, "//button[text()='Signup']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def verify_new_user(self):
        return self.driver.find_element(*self.new_user_text).is_displayed()

    # def verify_new_user(self):
    #     try:

    def enter_name_email(self, name, email):
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)

    def click_signup(self):
        self.driver.find_element(*self.signup_btn).click()