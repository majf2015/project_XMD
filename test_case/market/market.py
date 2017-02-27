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
        self.test_data.read(r"E:/project_XMD/test_data/market/market_test_data.conf")
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

    def test_create_coupon(self):
        coupon_data =  dict(self.test_data.items('Coupon'))
        time.sleep(1)
        self.browser.find_element_by_css_selector("div[nav = \"sellCenter\"]").click()
        self.browser.find_element_by_css_selector("li[nav = \"ordinaryCouponSell\"]").click()
        time.sleep(1)
        self.browser.find_element_by_css_selector("a[class = \"toolButton info\"]").click()
        time.sleep(1)
        self.browser.find_element_by_id("couponName").send_keys(coupon_data["coupon_name"].decode('utf-8'))
        self.browser.find_element_by_id("actValueOfMoney").send_keys(coupon_data["off_money"])
        self.browser.find_element_by_id("consumeOfMoneyType").send_keys(coupon_data["off_money_condition"])
        self.browser.find_element_by_id("commissionOfRedpackShare").send_keys(coupon_data["commission"])
        self.browser.find_element_by_xpath("//div[@class = 'ope']/a[1]").click()
        time.sleep(1)

    def test_create_lucky_wheel(self):
        coupon_data =  dict(self.test_data.items('luckyWheel'))
        time.sleep(1)
        self.browser.find_element_by_css_selector("div[nav = \"sellCenter\"]").click()
        time.sleep(0.5)
        self.browser.find_element_by_css_selector("li[nav = \"luckyWheel\"]").click()
        time.sleep(0.5)
        self.browser.find_element_by_css_selector("a[class = \"toolButton info\"]").click()
        time.sleep(0.5)
        self.browser.find_element_by_name("aticName").send_keys(coupon_data["wheel_name"].decode('utf-8'))
        #self.browser.find_element_by_name("addTime").clear()
        #self.browser.find_element_by_name("addTime").send_keys(coupon_data["wheel_time"])
        #time.sleep(5)
        #self.browser.find_element_by_xpath("//div[@class = 'ranges']/div[@class = 'range_inputs']"
        #                                   "/button[1]").click()
        #self.browser.find_element_by_xpath("//button[@class = 'applyBtn btn btn-sm btn-success']").click()
        #self.browser.find_element_by_class_name("applyBtn.btn.btn-sm.btn-success").click()
        #self.browser.find_element_by_css_selector("button[class = \'applyBtn btn btn-sm btn-success\']").click()
        #self.browser.find_element_by_link_text("确定").click()
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[1]/td[@ class = 'name']/input")\
            .send_keys(coupon_data["wheel_point"])
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[1]/td[@ class = 'number']/input")\
            .send_keys(coupon_data["wheel_point_number"])
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[1]/td[@ class = 'concept']/input")\
            .send_keys(coupon_data["wheel_point_concept"])
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[2]/td[@ class = 'name']/input")\
            .send_keys(coupon_data["wheel_prize"])
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[2]/td[@ class = 'number']/input")\
            .send_keys(coupon_data["wheel_prize_number"])
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[2]/td[@ class = 'concept']/input")\
            .send_keys(coupon_data["wheel_prize_concept"])
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[3]/td[@ class = 'number']/input")\
            .send_keys(coupon_data["wheel_coupon_number"])
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[3]/td[@ class = 'concept']/input")\
            .send_keys(coupon_data["wheel_coupon_concept"])
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[4]/td[@ class = 'number']/input")\
            .send_keys(coupon_data["wheel_item_number"])
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[4]/td[@ class = 'concept']/input")\
            .send_keys(coupon_data["wheel_item_concept"])
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[5]/td[@ class = 'concept']/input")\
            .send_keys(coupon_data["wheel_once_more_concept"])
        self.browser.find_element_by_xpath("//tbody[@class = 'add']/tr[6]/td[@ class = 'concept']/input")\
            .send_keys(coupon_data["wheel_no_win_concept"])
        self.browser.find_element_by_id("editActContent").send_keys(coupon_data["wheel_content"].decode('utf-8'))
        self.browser.find_element_by_xpath("//div[@id = 'editDialSellModal']/div/div[@class = 'footer']/a[1]").click()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Market)
    unittest.TextTestRunner(verbosity=2).run(suite)










