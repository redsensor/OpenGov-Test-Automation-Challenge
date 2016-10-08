import time

from core.helpers.GenericMethods import GenericActions
from selenium.webdriver.common.by import By


class AdminLoginLocators(object):
    # Page locators and variables

    ADD_NEW_TOUR_LINK = './/*[@id="Tours"]/li[2]/a'
    TOURS_MENU = './/ul/li/a/span[text()="Tours"]'
    TOUR_NAME_FIELD = './/div/input[@name="tourname"]'
    TOUR_TYPE_SELECTOR = './/label[text()="Tour Type"]//following-sibling::div/div/a'
    # ADVENTURE_LIST_ITEM = './/*[contains(text(),"Adventure")]'
    LOCATION_10_FIELD = './/label[contains(text(),"Location 10")]//following-sibling::div/div/a'
    ADULTS_QUANTITY_FIELD = './/tr/td[text()="Quantity"]/following-sibling::td/input[@name="maxadult"]'
    ADULTS_PRICE_FIELD = './/tr/td[text()="Price"]/following-sibling::td/input[@name="adultprice"]'
    SUBMIT_TOUR_FORM_BUTTON = './/div/button[contains(text(),"Submit")]'

    LOGIN = "admin@phptravels.com"
    PASSWORD = "demoadmin"
    EMAIL_INPUT = '//input[@name="email"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    LOGIN_BUTTON = '//button/span[text()="Login"]'
    ADMIN_PANEL_BUTTON = '//button/small[contains(text(),"admin")]'


class AdminLoginGo(GenericActions):

    # defining all methods for the page

    def __init__(self, driver, base_url):
        super(AdminLoginGo, self).__init__(driver)
        self.driver = driver
        self.driver.get(base_url)

    def go_to_admin_panel(self):
        admin_panel_button = self.driver.find_element(By.XPATH, AdminLoginLocators.ADMIN_PANEL_BUTTON)
        admin_panel_button.click()
        return self

    def set_email(self):
        email_input = self.driver.find_element(By.XPATH, AdminLoginLocators.EMAIL_INPUT)
        email_input.send_keys(AdminLoginLocators.LOGIN)

    def set_password(self):
        password_input = self.driver.find_element(By.XPATH, AdminLoginLocators.PASSWORD_INPUT)
        password_input.send_keys(AdminLoginLocators.PASSWORD)

    def click_login(self):
        login_button = self.driver.find_element(By.XPATH, AdminLoginLocators.LOGIN_BUTTON)
        login_button.click()

    def log_in_as_admin(self):
        self.focus_on_current_page() # setting focus on a new tab
        self.set_email()
        self.set_password()
        self.click_login()
        return self

    def add_new_tour(self):
        tours_menu = self.driver.find_element(By.XPATH, AdminLoginLocators.TOURS_MENU)
        add_new_tour_link = self.driver.find_element(By.XPATH, AdminLoginLocators.ADD_NEW_TOUR_LINK)
        tours_menu.click()
        """WebDriverWait(self.driver, 5)\
            .until(expected_conditions.presence_of_element_located((By.XPATH, AdminLoginLocators.ADD_NEW_TOUR_LINK)))"""
        time.sleep(3)
        add_new_tour_link.click()
        return self

    def fill_tour_form(self, tour_name_, adults_quantity_, adults_price_):

        self.focus_on_current_page() # setting focus on a new tab
        tour_name = self.driver.find_element(By.XPATH, AdminLoginLocators.TOUR_NAME_FIELD)
        tour_type_selector = self.driver.find_element(By.XPATH, AdminLoginLocators.TOUR_TYPE_SELECTOR)
        location_ten_selector = self.driver.find_element(By.XPATH, AdminLoginLocators.LOCATION_10_FIELD)
        adults_quantity = self.driver.find_element(By.XPATH, AdminLoginLocators.ADULTS_QUANTITY_FIELD)
        adults_price = self.driver.find_element(By.XPATH, AdminLoginLocators.ADULTS_PRICE_FIELD)

        tour_name.send_keys(tour_name_)
        adults_quantity.send_keys(adults_quantity_)
        adults_price.send_keys(adults_price_)
        tour_type_selector.click()

        # selecting first item from list
        GenericActions.key_down_key_enter_press(self)

        location_ten_selector.click()
        GenericActions.key_down_key_enter_press(self)

        # tour_type = self.driver.find_element(By.XPATH, AdminLoginLocators.ADVENTURE_LIST_ITEM)
        # tour_type.click()

    def submit_tour_form(self):
        tour_submit_button = self.driver.find_element(By.XPATH, AdminLoginLocators.SUBMIT_TOUR_FORM_BUTTON)
        tour_submit_button.click()

    def create_new_tour(self, tour_name_, adults_quantity, adults_price):
        self.add_new_tour()
        self.fill_tour_form(tour_name_, adults_quantity, adults_price)
        self.submit_tour_form()
        return self

