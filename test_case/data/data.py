# -*- coding: utf-8 -*-
import ConfigParser
import time
import unittest

import login


class Data(unittest.TestCase):
    def setUp(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(r"E:/project_XMD/config.conf")
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(r"E:/project_XMD/test_data/data/data_test_data.conf")
        self.debug = int(self.conf.get('Debug','debug'))
        self.Browser = login.Login()
        self.Browser.login()
        self.browser = self.Browser.browser

    def tearDown(self):
        self.browser.quit()

    #核对注册用户总数
    def test_registered(self):
        time.sleep(1)
        self.browser.find_element_by_css_selector("div[nav = \"dataStatistics\"]").click()
        self.browser.find_element_by_css_selector("li[nav=\"registeredDataStatistics\"]").click()
        time.sleep(1)
        regis = filter(str.isdigit,str(self.browser.find_element_by_xpath("//td[@class = 'total']").text.encode('utf-8')))
        if self.test_data.get('DataAnalysis','register') == regis:
            print "register data right"

    #查看详情、核对详情记录总数
    def test_phone_registered(self):
        time.sleep(1.5)
        self.browser.find_element_by_css_selector("div[nav = \"dataStatistics\"").click()
        self.browser.find_element_by_css_selector("li[nav=\"registeredDataStatistics\"").click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//td[@class = 'total']/a").click()
        time.sleep(1)
        phone_regis = len(self.browser.find_elements_by_xpath("//div[@id  = 'dataListTable']/table/tbody/tr"))
        right_data = int(self.test_data.get('DataAnalysis','phone_register'))
        if right_data == phone_regis or phone_regis == 20:
            print "phone_register data right"


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Data)
    unittest.TextTestRunner(verbosity=2).run(suite)






