# -*- coding: utf-8 -*-
import login,global_attributes,time,unittest


class Home(unittest.TestCase):
    def setUp(self):
        self.Browser = login.Login()
        self.Browser.login()
        self.browser = self.Browser.browser

    def tearDown(self):
        self.browser.quit()

    def test_menu(self):
        time.sleep(1)
        self.browser.find_element_by_css_selector("div[nav = \"dataStatistics\"").click()
        self.browser.find_element_by_css_selector("li[nav=\"registeredDataStatistics\"").click()

        time.sleep(1)