from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select

import unittest

import time

class StoreTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.shipt.com")

    def test_Add(self):

        elem = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_link_text("Log In"))
        elem.click()


        time.sleep(10)
        self.driver.find_element_by_css_selector("input[type='email']").send_keys('qatest@shipt.com')
        self.driver.find_element_by_css_selector("input[type='password']").send_keys('Sh1pt123!')
        self.driver.find_element_by_id("start_shopping_login_button").click()


        elem = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_xpath("//div/form/label"))
        elem.send_keys('apple')

        element1 = WebDriverWait(self.driver, 30).until(lambda driver: self.driver.find_element_by_xpath("//link[contains(@href,'/apple-touch-icon-57x57.png')]"))
        element1.click()



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

