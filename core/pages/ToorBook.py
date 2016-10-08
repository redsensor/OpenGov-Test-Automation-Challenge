import time
from webbrowser import browser

from core.helpers.GenericMethods import GenericActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ToorBookLocators(object):
    # Page locators and variables

    HOMEPAGE_BUTTON = '//h3[text()="HOMEPAGE"]/following-sibling::div//button'
    MY_ACCOUNT_DROPDOWN = './/li[contains(@class, "dropdown")]/a[contains(text(),"Account")]'
    LOGIN_BUTTON = './/ul/li/a[contains(text(),"Login")]'

    LOGIN = "admin@phptravels.com"
    PASSWORD = "demoadmin"
    EMAIL_INPUT = '//input[@name="email"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    PAGE_HEAD = './/form[@id="loginfrm"]'


class ToorBookGo(GenericActions):

    # defining all methods for the page

    def __init__(self, driver, base_url):
        super(ToorBookGo, self).__init__(driver)
        self.driver = driver
        self.driver.get(base_url)

    def go_to_home_page(self):
        homepage_button = self.driver.find_element(By.XPATH, ToorBookLocators.HOMEPAGE_BUTTON)
        homepage_button.click()
        GenericActions.focus_on_current_page(self)
        return self

    def go_to_login_page(self):
        my_account_button = self.driver.find_element(By.XPATH, ToorBookLocators.MY_ACCOUNT_DROPDOWN)
        my_account_button.click()
        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, ToorBookLocators.LOGIN_BUTTON)
        login_button.click()
        GenericActions.focus_on_current_page(self)
        return self

    def set_email(self, email_):
        time.sleep(3)
        self.focus_on_current_page()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, ToorBookLocators.EMAIL_INPUT)))
        email_input = self.driver.find_element(By.XPATH, ToorBookLocators.EMAIL_INPUT)
        email_input.send_keys(email_)

    def set_password(self, password_):
        password_input = self.driver.find_element(By.XPATH, ToorBookLocators.PASSWORD_INPUT)
        password_input.send_keys(password_)

    def click_login(self):
        self.driver.execute_script("document.getElementsByTagName('button')[1].click()")

    def log_in_as_customer(self, email_, password_):
        self.focus_on_current_page() # setting focus on a new tab
        self.set_email(email_)
        self.set_password(password_)
        self.click_login()
        return self

