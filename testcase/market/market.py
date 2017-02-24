# -*- coding: utf-8 -*-
import ConfigParser
import time
import unittest

import login


class Market(unittest.TestCase):
    def setUp(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(r"E:/project_XMD/config.conf")
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(r"E:/project_XMD/SQL/market/market_test_data.conf")
        self.debug = int(self.conf.get('Debug','debug'))
        self.Browser = login.Login()
        self.Browser.login()
        self.browser = self.Browser.browser

    def tearDown(self):
        self.browser.quit()

    #创建点钟券
    def test_create_paid_coupon(self):
        coupon_data =  dict(self.test_data.items('Paid_coupon'))
        time.sleep(1)
        self.browser.find_element_by_css_selector("div[nav = \"sellCenter\"]").click()
        self.browser.find_element_by_css_selector("li[nav = \"paidCouponSell\"]").click()
        time.sleep(1)
        self.browser.find_element_by_css_selector("a[class = \"toolButton info\"]").click()
        self.browser.find_element_by_id("editActValue").send_keys(coupon_data["act_value"])
        self.browser.find_element_by_id("editActConsumeMoney").send_keys(coupon_data["consume_money"])
        self.browser.find_element_by_id("couponCommission").send_keys(coupon_data["commission"])
        self.browser.find_element_by_xpath("//div[@id = 'couponEditModal']/div/div[@class = 'footer']/a[1]").click()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Market)
    unittest.TextTestRunner(verbosity=2).run(suite)










