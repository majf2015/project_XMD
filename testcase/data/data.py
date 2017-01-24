# -*- coding: utf-8 -*-
import login,time,unittest
import ConfigParser


class Data(unittest.TestCase):
    def setUp(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(r"E:/project_XMD/test_data.conf")
        self.debug = self.conf.get('Debug','debug')
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