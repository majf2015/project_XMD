# -*- coding: utf-8 -*-
import login,global_attributes,time,unittest


class Home(unittest.TestCase):
    def setUp(self):
        self.Browser = login.Login()
        self.Browser.login()
        self.browser = self.Browser.browser
        self.coupon_data = global_attributes.coupon_data
        self.coupon_phone = global_attributes.coupon_phone
        self.debug = global_attributes.debug

    def tearDown(self):
        self.browser.quit()

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





