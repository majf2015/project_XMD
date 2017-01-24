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

    def tearDown(self):
        self.browser.quit()


    def test_verify_coupon_no(self):
        coupon_data = dict(self.conf.items('Coupon'))
        for test_data in dict(self.conf.items('Coupon')):
            time.sleep(1)
            if self.debug:
                print test_data,':',coupon_data[test_data]
            self.browser.find_element_by_xpath("//input[@type = 'text']").send_keys(coupon_data[test_data])
            self.browser.find_element_by_css_selector( "a[class =\"toolButton info\"").click()
            time.sleep(1)
            self.browser.find_element_by_xpath("//tbody/tr/td[5]/i").click()
            self.browser.find_element_by_class_name("ok").click()
            time.sleep(1)
            self.browser.refresh()

    def test_verify_coupon_phone(self):
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@type = 'text']").send_keys(self.conf.get('Verify','phone'))
        self.browser.find_element_by_css_selector( "a[class =\"toolButton info\"").click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//tbody/tr/td[5]/i").click()
        self.browser.find_element_by_class_name("ok").click()

    def test_verify_order(self):
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@type = 'text']").send_keys(self.conf.get('Verify','order'))
        self.browser.find_element_by_css_selector( "a[class =\"toolButton info\"").click()
        time.sleep(1)
        self.browser.find_element_by_css_selector( "a[class =\"ok\"").click()

    def test_verify_prize(self):
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@type = 'text']").send_keys(self.conf.get('Verify','prize'))
        self.browser.find_element_by_css_selector( "a[class =\"toolButton info\"").click()
        time.sleep(1)
        self.browser.find_element_by_css_selector( "a[class =\"ok\"").click()


    def test_tech(self):
        time.sleep(1)
        tec = filter(str.isdigit,str(self.browser.find_element_by_xpath("//ul[@class='clearfix']/li[1]").text.encode('utf-8')))
        if self.conf.get('Tech','tech') == tec:
            print "tech data right"








