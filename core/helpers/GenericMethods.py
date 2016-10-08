from random import random

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumwrapper.BasePageElement import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import random, string


class GenericActions(object):

    def __init__(self, driver):
        self.driver = driver
        super(GenericActions, self).__init__()

    def scroll_to_element(self, element): # scroll to any element on the page
        target = self.driver.find_element(element)
        self.driver.execute_script("return arguments[0].scrollIntoView();", target)
        return self

    def key_down_key_enter_press(self): # invokes key down and enter press commands
        ActionChains(self.driver) \
            .send_keys(Keys.ARROW_DOWN)\
            .send_keys(Keys.ENTER)\
            .perform()
        return self

    def is_element_present_by_xpath(self, xpath): # check whether element is presented on the page
        try:
            self.driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            print("Element is not presented on the page!")
            return False
        return True

    @staticmethod
    def generate_random_word(length): # generating word with given length
        return ''.join(random.choice(string.lowercase) for i in range(length))

    def focus_on_current_page(self): # gives the focus to the current window and tab
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element);
        return self






