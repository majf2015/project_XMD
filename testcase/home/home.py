# -*- coding: utf-8 -*-
import login,ConfigParser,time,unittest


class Home(unittest.TestCase):
    def setUp(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(r"E:/project_XMD/test_data.conf")
        self.debug = int(self.conf.get('Debug','debug'))
        self.Browser = login.Login()
        self.Browser.login()
        self.browser = self.Browser.browser
        self.coupon_data =  dict(self.conf.items('Coupon'))
        self.coupon_phone = self.conf.get('Phone','phone')

    def test_verify_coupon_no(self):
        for test_data in self.coupon_data:
            time.sleep(1)
            if self.debug:
                print test_data,':',self.coupon_data[test_data]
            self.browser.find_element_by_xpath("//input[@type = 'text']").send_keys(self.coupon_data[test_data])
            self.browser.find_element_by_css_selector( "a[class =\"toolButton info\"").click()
            time.sleep(1)
            self.browser.find_element_by_xpath("//tbody/tr/td[5]/i").click()
            self.browser.find_element_by_class_name("ok").click()
            time.sleep(1)
            self.browser.refresh()

    def test_verify_coupon_phone(self):
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@type = 'text']").send_keys(self.coupon_phone)
        self.browser.find_element_by_css_selector( "a[class =\"toolButton info\"").click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//tbody/tr/td[5]/i").click()
        self.browser.find_element_by_class_name("ok").click()





