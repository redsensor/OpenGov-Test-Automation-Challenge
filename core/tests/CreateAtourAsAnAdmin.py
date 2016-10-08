import unittest
from random import randint

import nose
from faker import Factory
from core.pages import selenium_driver
from core.pages.AdminLogin import AdminLoginGo


class CreaAtourAsAnAdmin(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.driver.implicitly_wait(10)
        self.base_url = selenium_driver.base_url

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_create_tour_as_admin(self):
        AdminLoginGoPage = AdminLoginGo(self.driver, self.base_url)

        # instantiating fake data generator
        fake = Factory.create()
        test_tour = fake.name()

        AdminLoginGoPage\
            .go_to_admin_panel()\
            .log_in_as_admin()\
            .create_new_tour(test_tour, randint(0, 5), randint(100, 200))

        NEW_TOUR_NAME = self.driver.find_element_by_xpath('.//tr/td[text()="1"]/following-sibling::td/a[text()="' + test_tour + '"]')
        # checking whether we are on the proper page (tours management)
        self.assertIn("Tours Management", self.driver.title)
        # checking if the new tour name is presented and has the first position in the given list
        self.assertTrue(NEW_TOUR_NAME, "Created tour is not presented in the list!")

        # we can open the created tour and add more verifications next

if __name__ == "__main__":
    nose.main()