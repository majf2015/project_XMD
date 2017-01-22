# -*- coding: utf-8 -*-
import login,global_attributes,time,unittest


class Home(unittest.TestCase):
    def setUp(self):
        self.Browser = login.Login()
        self.Browser.login()
        self.browser = self.Browser.browser
        if global_attributes.debug:
            print self.browser

    def tearDown(self):
        self.browser.quit()

    def test_write_off_coupon(self):
        if global_attributes.debug:
            print self.browser
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@type = 'text']").send_keys('106341781024')
        self.browser.find_element_by_css_selector( "a[class =\"toolButton info\"").click()




