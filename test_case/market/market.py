# -*- coding: utf-8 -*-
import ConfigParser, time, unittest, os, sys

import public_module


class Market(unittest.TestCase):
    def setUp(self):
        self.public = public_module.Public()
        self.public.login()
        self.conf = self.public.conf
        self.project_path = self.public.project_path
        self.browser = self.public.browser
        self.debug = self.public.debug
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(os.path.join(self.project_path,'test_data\market\market_test_data.conf'))

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

    #创建优惠券
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

    #创建大转盘活动
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

     #大转盘活动上线操作
    def test_lucky_wheel_online(self):
        time.sleep(1)
        self.browser.find_element_by_css_selector("div[nav = \"sellCenter\"]").click()
        time.sleep(0.5)
        self.browser.find_element_by_css_selector("li[nav = \"luckyWheel\"]").click()
        time.sleep(0.5)
        tr = self.browser.find_elements_by_xpath("//div[@id = 'dataListTable']/table/tbody/tr")
        tr_last = self.browser.find_element_by_xpath\
            ("//div[@id = 'dataListTable']/table/tbody/tr[%s]/td[6]/a[1]" % len(tr)).click()
        time.sleep(0.5)

        result = self.browser.find_element_by_xpath\
            ("//div[@id = 'dataListTable']/table/tbody/tr[%s]/td[4]" % len(tr)).text
        if result  == u"上线":
            print 'test_lucky_wheel_online'

        else:
            raise Exception("error")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Market)
    unittest.TextTestRunner(verbosity=2).run(suite)










