# -*- coding: utf-8 -*-
import ConfigParser, time, unittest, os,public_module
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Publicity(unittest.TestCase):
    def setUp(self):
        self.public = public_module.Public()
        self.public.login()
        self.conf = self.public.conf
        self.project_path = self.public.project_path
        self.browser = self.public.browser
        self.debug = self.public.debug
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(os.path.join(self.project_path,'test_data\publicity\publicity_test_data.conf'))

    def tearDown(self):
        self.browser.quit()

    #群发消息
    def test_sms(self):
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[nav = \"propaganda\"]")))
        self.browser.find_element_by_css_selector("div[nav = \"propaganda\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "li[nav = \"massMessageSendRecord\"]")))
        self.browser.find_element_by_css_selector("li[nav = \"massMessageSendRecord\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "a[class = \"toolButton info\"]")))
        self.browser.find_element_by_css_selector("a[class = \"toolButton info\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.ID, "actSelector")))
        self.browser.find_element_by_id("actSelector").click()
        self.browser.find_element_by_xpath("//select[@id = 'actSelector']/option[2]").click()
        self.browser.find_element_by_id("msgContent").send_keys(u"自动化测试发送微信信息")
        self.browser.find_element_by_xpath("//h3[@class = 'title btns']/a[2]").click()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Publicity)
    unittest.TextTestRunner(verbosity=2).run(suite)










