# -*- coding: utf-8 -*-
import ConfigParser, time, unittest, os,public_module
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Tech(unittest.TestCase):
    def setUp(self):
        self.public = public_module.Public()
        self.public.login()
        self.conf = self.public.conf
        self.project_path = self.public.project_path
        self.browser = self.public.browser
        self.debug = self.public.debug
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(os.path.join(self.project_path,'test_data\\tech\\tech_test_data.conf'))

    def tearDown(self):
        self.browser.quit()

    #核对技师忙/闲状态数
    def test_tech(self):
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[nav = \"techAdmin\"]")))
        self.browser.find_element_by_css_selector("div[nav = \"techAdmin\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "li[nav = \"techList\"]")))
        self.browser.find_element_by_css_selector("li[nav = \"techList\"]").click()
        free_tec = len(self.browser.find_elements_by_xpath("//ul[@id = 'freeTechList']/li"))
        if self.test_data.get('Tech','free_tech') == str(free_tec):
            print "free tech data right"
        else:
            raise Exception("error:free tech data")
        busy_tec = len(self.browser.find_elements_by_xpath("//ul[@id = 'busyTechList']/li"))
        if self.test_data.get('Tech','busy_tech') == str(busy_tec):
            print "busy tech data right"
        else:
            raise Exception("error:busy tech data")


    #筛选技师(未完成)
    def test_tech_filter(self):
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[nav = \"techAdmin\"]")))
        self.browser.find_element_by_css_selector("div[nav = \"techAdmin\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "li[nav = \"techList\"]")))
        self.browser.find_element_by_css_selector("li[nav = \"techList\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class = 'title']/select")))
        self.browser.find_element_by_xpath("//div[@class = 'title']/select").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class = 'title']/select/option[2]")))
        self.browser.find_element_by_xpath("//div[@class = 'title']/select/option[2]").click()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Tech)
    unittest.TextTestRunner(verbosity=2).run(suite)










