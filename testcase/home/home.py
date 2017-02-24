# -*- coding: utf-8 -*-
import ConfigParser
import time
import unittest

import login


class Home(unittest.TestCase):
    def setUp(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(r"E:/project_XMD/config.conf")
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(r"E:/project_XMD/SQL/home/home_test_data.conf")
        self.debug = int(self.conf.get('Debug','debug'))
        self.Browser = login.Login()
        self.Browser.login()
        self.browser = self.Browser.browser

    def tearDown(self):
        self.browser.quit()

    #核对技师总数、忙/闲状态技师数
    def test_tech(self):
        time.sleep(1)
        tec = filter(str.isdigit,str(self.browser.find_element_by_xpath("//ul[@class='clearfix']/li[1]")
                                     .text.encode('utf-8')))
        if self.test_data.get('Tech','tech') == tec:
            print "tech data right"
        busy_tec = filter(str.isdigit,str(self.browser.find_element_by_xpath("//ul[@class='clearfix']/li[2]")
                                          .text.encode('utf-8')))
        if self.test_data.get('Tech','busy_tech') == busy_tec:
            print "busy_tech data right"
        free_tec = filter(str.isdigit,str(self.browser.find_element_by_xpath("//ul[@class='clearfix']/li[3]")
                                          .text.encode('utf-8')))
        if self.test_data.get('Tech','free_tech') == free_tec:
            print "free_tech data right"

    #核销普通,注册,分享,点钟券,大转盘项、限时抢项目券,网店价购买项目
    def test_verify_coupon_no(self):
        coupon_data = dict(self.test_data.items('Coupon'))
        for test_data in dict(self.test_data.items('Coupon')):
            time.sleep(1)
            if self.debug:
                print test_data,':',coupon_data[test_data]
            self.browser.find_element_by_xpath("//input[@type = 'text']").send_keys(coupon_data[test_data])
            self.browser.find_element_by_css_selector( "a[class =\"toolButton info\"]").click()
            time.sleep(1)
            self.browser.find_element_by_xpath("//tbody/tr/td[5]/i").click()
            self.browser.find_element_by_class_name("ok").click()
            time.sleep(1)
            self.browser.refresh()

    #核销通过手机号查询的券
    def test_verify_coupon_phone(self):
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@type = 'text']").send_keys(self.test_data.get('Verify','phone'))
        self.browser.find_element_by_css_selector( "a[class =\"toolButton info\"]").click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//tbody/tr/td[5]/i").click()
        self.browser.find_element_by_class_name("ok").click()
        if self.debug:
            print 'verify_coupon_phone',':',self.test_data.get('Verify','phone')

    #核销付费预约
    def test_verify_order(self):
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@type = 'text']").send_keys(self.test_data.get('Verify','order'))
        self.browser.find_element_by_css_selector( "a[class =\"toolButton info\"").click()
        time.sleep(1)
        self.browser.find_element_by_css_selector( "a[class =\"ok\"]").click()
        if self.debug:
            print 'verify_order',':',self.test_data.get('Verify','order')

    #核销大转盘奖品
    def test_verify_prize(self):
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@type = 'text']").send_keys(self.test_data.get('Verify','prize'))
        self.browser.find_element_by_css_selector( "a[class =\"toolButton info\"]").click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//div[@id = 'luckyWheelVerificationModal']/div/div[@class = 'footer']/a[@class = 'ok']").click()
        if self.debug:
            print 'verify_prize',':',self.test_data.get('Verify','prize')

    #买单提醒核对数据、确认提醒、异常提醒
    def test_bill_reminder(self):
        time.sleep(1)
        if self.browser.find_element_by_xpath("//div[@class = 'dataTable']/table/tbody/tr").text \
                ==self.test_data.get('Bill','bill_reminder').decode('utf-8'):
            print 'bill reminder data right'
        time.sleep(1)
        self.browser.find_element_by_xpath("//div[@class = 'dataTable']/table/tbody/tr/td[6]/a[1]").click()
        self.browser.find_element_by_id("confirm-fast-pay-remark").send_keys(u"确认")
        self.browser.find_element_by_xpath("//div[@id = 'confirmFastPayModal']"
                                           "/div/div[@class = 'footer']/a[@class = 'ok']").click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//div[@class = 'dataTable']/table/tbody/tr/td[6]/a[2]").click()
        self.browser.find_element_by_id("confirm-fast-pay-remark").send_keys(u"异常")
        time.sleep(1)
        self.browser.find_element_by_xpath("//div[@id = 'confirmFastPayModal']"
                                           "/div/div[@class = 'footer']/a[@class = 'ok']").click()
        print 'pass and unpass right'

    #通过时间控件及技师编号筛选出订单、核对查询记录总数、核对第一条记录数据
    def test_order_list(self):
        time.sleep(1)
        self.browser.find_element_by_xpath("//div[@class = 'searchForm time']/input[@type = 'text']").clear()
        self.browser.find_element_by_xpath("//div[@class = 'searchForm time']/input[@type = 'text']").\
            send_keys(self.test_data.get('Order','time').decode('utf-8'))
        self.browser.find_element_by_xpath("//button[@class = 'applyBtn btn btn-sm btn-success']").click()
        self.browser.find_element_by_id('search-serial').send_keys(self.test_data.get('Order','tech_no'))
        self.browser.find_element_by_xpath("//div[@class = 'searchForm name']/a").click()
        records =  len(self.browser.find_elements_by_xpath("//div[@id = 'orderListDataTable']/table/tbody/tr"))
        right_data_records = int(self.test_data.get('Order','records'))
        first_record = self.browser.find_element_by_xpath("//div[@id = 'orderListDataTable']/table/tbody/tr").text
        right_data_first_record = self.test_data.get('Order','first_record').decode('utf-8')
        if records == right_data_records:
            print 'order records right'
        if first_record == right_data_first_record:
            print 'order first_record right'


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Home)
    unittest.TextTestRunner(verbosity=2).run(suite)










