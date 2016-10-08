import unittest
from random import randint

import time

import nose
import faker
from core.pages.ToorBook import ToorBookGo
from core.pages.UserSignUp import UserSignUpGo
from core.helpers.GenericMethods import GenericActions
from faker import Factory
from core.pages import selenium_driver
from selenium.webdriver.common.by import By
import random, string


class BookATourtAsCustomerGo(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.driver.implicitly_wait(10)
        self.base_url = selenium_driver.base_url

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_book_tour_as_customer(self):
        #GenA = GenericActions(self.driver)
        ToorBookGoPage = ToorBookGo(self.driver, self.base_url)

        ToorBookGoPage\
            .go_to_home_page()\
            .go_to_login_page()\
            .log_in_as_customer("user@phptravels.com", "demouser")
        time.sleep(100)


        """name = self.driver.find_element_by_xpath('.//div/h3[@class="RTL" and contains(text(),"' + f_name + " " + l_name + '")]')
        f_name_input = self.driver.find_element_by_name('firstname').get_attribute('value').encode('utf-8')
        l_name_input = self.driver.find_element_by_name('lastname').get_attribute('value').encode('utf-8')
        phone_input = self.driver.find_element_by_name('phone').get_attribute('value').encode('utf-8')
        email_input = self.driver.find_element_by_name('email').get_attribute('value').encode('utf-8')

        # checking whether the new name is presented on the page
        self.assertTrue(name, "Name is not presented on page!")
        # checking whether the data in inputs is correct
        self.assertEqual(f_name, f_name_input, "First names are different")
        self.assertEqual(l_name, l_name_input, "Last names are different")
        self.assertEqual(p_number, phone_input, "Phones are different")
        self.assertEqual(email, email_input, "Emails are different")"""

        # we can also create test that will log out, log in and check if logging in is possible with given data

if __name__ == "__main__":
    nose.main()