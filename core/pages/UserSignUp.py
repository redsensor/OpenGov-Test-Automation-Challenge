import time

from core.helpers.GenericMethods import GenericActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserSignUpLocators(object):

    HOMEPAGE_BUTTON = '//h3[text()="HOMEPAGE"]/following-sibling::div//button'
    MY_ACCOUNT_DROPDOWN = './/li[contains(@class, "dropdown")]/a[contains(text(),"Account")]'
    SIGN_UP_BUTTON = './/ul/li/a[contains(text(),"Sign Up")]'

    FIRST_NAME_INPUT = './/*[@id="headersignupform"]/div[3]/input'
    LAST_NAME_INPUT = './/*[@id="headersignupform"]/div[4]/input'
    MOBILE_NUMBER_INPUT = './/*[@id="headersignupform"]/div[5]/input'
    EMAIL_INPUT = './/*[@id="headersignupform"]/div[6]/input'
    PASSWORD_INPUT = './/*[@id="headersignupform"]/div[7]/input'
    CONFIRM_PASSWORD_INPUT = './/*[@id="headersignupform"]/div[8]/input'
    SIGN_UP_BUTTON_REGISTER = './/div/button[contains(text(),"Sign Up")]'
    MY_PROFILE_TAB = './/ul/li/a[contains(@href,"profile")]'


class UserSignUpGo(GenericActions):

    # defining all methods for the page

    def __init__(self, driver, base_url):
        super(UserSignUpGo, self).__init__(driver)
        self.driver = driver
        self.driver.get(base_url)

    def go_to_home_page(self):
        homepage_button = self.driver.find_element(By.XPATH, UserSignUpLocators.HOMEPAGE_BUTTON)
        homepage_button.click()
        GenericActions.focus_on_current_page(self)
        return self

    def go_to_sign_up_page(self):
        my_account_button = self.driver.find_element(By.XPATH, UserSignUpLocators.MY_ACCOUNT_DROPDOWN)
        self.js_click(my_account_button)
        time.sleep(1)
        sign_up_button = self.driver.find_element(By.XPATH, UserSignUpLocators.SIGN_UP_BUTTON)
        self.js_click(sign_up_button)
        GenericActions.focus_on_current_page(self)
        return self

    def fill_sign_up_form(self, first_name_, last_name_, mobile_number_, email_, password_, confirm_password_):
        first_name = self.driver.find_element(By.XPATH, UserSignUpLocators.FIRST_NAME_INPUT)
        last_name = self.driver.find_element(By.XPATH, UserSignUpLocators.LAST_NAME_INPUT)
        mobile_number = self.driver.find_element(By.XPATH, UserSignUpLocators.MOBILE_NUMBER_INPUT)
        email = self.driver.find_element(By.XPATH, UserSignUpLocators.EMAIL_INPUT)
        password = self.driver.find_element(By.XPATH, UserSignUpLocators.PASSWORD_INPUT)
        confirm_password = self.driver.find_element(By.XPATH, UserSignUpLocators.CONFIRM_PASSWORD_INPUT)
        first_name.send_keys(first_name_)
        last_name.send_keys(last_name_)
        mobile_number.send_keys(mobile_number_)
        email.send_keys(email_)
        password.send_keys(password_)
        confirm_password.send_keys(confirm_password_)
        return self

    def submit_sign_up_form(self):
        sign_up_button_register = self.driver.find_element(By.XPATH, UserSignUpLocators.SIGN_UP_BUTTON_REGISTER)
        sign_up_button_register.click()
        return self

    def go_to_my_profile(self):
        my_profile_tab = self.driver.find_element(By.XPATH, UserSignUpLocators.MY_PROFILE_TAB)
        my_profile_tab.click()
        return self





