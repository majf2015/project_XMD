# -*- coding: utf-8 -*-
import ConfigParser, time, unittest, os,public_module
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

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
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[nav = \"sellCenter\"]")))
        self.browser.find_element_by_css_selector("div[nav = \"sellCenter\"]").click()
        self.browser.find_element_by_css_selector("li[nav = \"paidCouponSell\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "a[class = \"toolButton info\"]")))
        self.browser.find_element_by_css_selector("a[class = \"toolButton info\"]").click()
        self.browser.find_element_by_id("editActValue").send_keys(coupon_data["act_value"])
        self.browser.find_element_by_id("editActConsumeMoney").send_keys(coupon_data["consume_money"])
        self.browser.find_element_by_id("couponCommission").send_keys(coupon_data["commission"])
        self.browser.find_element_by_xpath("//div[@id = 'couponEditModal']/div/div[@class = 'footer']/a[2]").click()
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located
             ((By.XPATH, "//div[@id = 'dataListTable']/table/tbody/tr[1]/td[1]")))
        result_name = self.browser.find_element_by_xpath("//div[@id = 'dataListTable']/table/tbody/tr[1]/td[1]").text
        if result_name ==  u"50元点钟券(50元抵100元)":
            print 'test_create_paid_coupon'
        else:
            raise Exception("error:test_create_paid_coupon")
    #点钟券上线操作
    def test_paid_coupon_online(self):
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[nav = \"sellCenter\"]")))
        self.browser.find_element_by_css_selector("div[nav = \"sellCenter\"]").click()
        self.browser.find_element_by_css_selector("li[nav = \"paidCouponSell\"]").click()
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located
             ((By.XPATH, "//div[@id = 'dataListTable']/table/tbody/tr[1]/td[7]/a[1]")))
        self.browser.find_element_by_xpath("//div[@id = 'dataListTable']/table/tbody/tr[1]/td[7]/a[1]").click()
        self.browser.find_element_by_class_name("ok").click()
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located
             ((By.XPATH, "//div[@id = 'dataListTable']/table/tbody/tr[1]/td[3]")))
        result_name = self.browser.find_element_by_xpath("//div[@id = 'dataListTable']/table/tbody/tr[1]/td[3]").text
        if result_name ==  u"使用中":
            print 'test_paid_coupon_online'
        else:
            raise Exception("error:test_paid_coupon_online")

    #创建优惠券
    def test_create_coupon(self):
        coupon_data =  dict(self.test_data.items('Coupon'))
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[nav = \"sellCenter\"]")))
        self.browser.find_element_by_css_selector("div[nav = \"sellCenter\"]").click()
        self.browser.find_element_by_css_selector("li[nav = \"ordinaryCouponSell\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "a[class = \"toolButton info\"]")))
        self.browser.find_element_by_css_selector("a[class = \"toolButton info\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.ID, "couponName")))
        self.browser.find_element_by_id("couponName").send_keys(coupon_data["coupon_name"].decode('utf-8'))
        self.browser.find_element_by_id("actValueOfMoney").send_keys(coupon_data["off_money"])
        self.browser.find_element_by_id("consumeOfMoneyType").send_keys(coupon_data["off_money_condition"])
        self.browser.find_element_by_id("commissionOfRedpackShare").send_keys(coupon_data["commission"])
        self.browser.find_element_by_xpath("//div[@class = 'ope']/a[2]").click()
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located
             ((By.XPATH, "//div[@id = 'dataListTable']/table/tbody/tr[1]/td[2]")))
        result_name = self.browser.find_element_by_xpath("//div[@id = 'dataListTable']/table/tbody/tr[1]/td[2]").text
        if result_name ==  u"自动增加现金分享(分享有礼券)":
            print 'test_create_coupon'
        else:
            raise Exception("error:test_create_coupon")

    #优惠券上线操作
    def test_coupon_online(self):
        WebDriverWait(self.browser, 50).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[nav = \"sellCenter\"]")))
        self.browser.find_element_by_css_selector("div[nav = \"sellCenter\"]").click()
        self.browser.find_element_by_css_selector("li[nav = \"ordinaryCouponSell\"]").click()
        WebDriverWait(self.browser, 50).until(expected_conditions.visibility_of_element_located
             ((By.XPATH, "//div[@id = 'dataListTable']/table/tbody/tr[1]/td[9]/a[2]")))
        self.browser.find_element_by_xpath("//div[@id = 'dataListTable']/table/tbody/tr[1]/td[9]/a[2]").click()
        self.browser.find_element_by_class_name("ok").click()
        WebDriverWait(self.browser, 50).until(expected_conditions.visibility_of_element_located
             ((By.XPATH, "//div[@id = 'dataListTable']/table/tbody/tr[1]/td[5]")))
        result_name = self.browser.find_element_by_xpath("//div[@id = 'dataListTable']/table/tbody/tr[1]/td[5]").text
        if result_name ==  u"使用中":
            print 'test_coupon_online'
        else:
            raise Exception("error:test_coupon_online")
    #创建大转盘活动
    def test_create_lucky_wheel(self):
        coupon_data =  dict(self.test_data.items('luckyWheel'))
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[nav = \"sellCenter\"]")))
        self.browser.find_element_by_css_selector("div[nav = \"sellCenter\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "li[nav = \"luckyWheel\"]")))
        self.browser.find_element_by_css_selector("li[nav = \"luckyWheel\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "a[class = \"toolButton info\"]")))
        self.browser.find_element_by_css_selector("a[class = \"toolButton info\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.NAME, "aticName")))
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
        self.browser.find_element_by_xpath("//div[@id = 'editDialSellModal']/div/div[@class = 'footer']/a[2]").click()
        time.sleep(2)
        result_name = self.browser.find_element_by_xpath\
            ("//div[@id = 'dataListTable']/table/tbody/tr[1]/td[2]").text
        if result_name  == u"自动增加大转盘":
            print 'test_create_lucky_wheel'
        else:
            raise Exception("error:test_create_lucky_wheel")

     #大转盘活动上线操作
    def test_lucky_wheel_online(self):
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[nav = \"sellCenter\"]")))
        self.browser.find_element_by_css_selector("div[nav = \"sellCenter\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "li[nav = \"luckyWheel\"]")))
        self.browser.find_element_by_css_selector("li[nav = \"luckyWheel\"]").click()
        WebDriverWait(self.browser, 5).until\
            (expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id = 'dataListTable']/table/tbody/tr")))
        self.browser.find_element_by_xpath\
            ("//div[@id = 'dataListTable']/table/tbody/tr[1]/td[6]/a[1]").click()
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located
             ((By.XPATH, "//div[@id = 'dataListTable']/table/tbody/tr[1]/td[4]")))
        result_status = self.browser.find_element_by_xpath\
            ("//div[@id = 'dataListTable']/table/tbody/tr[1]/td[4]").text
        if result_status  == u"上线":
            print 'test_lucky_wheel_online'
        else:
            raise Exception("error:test_lucky_wheel_online")

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
    suite = unittest.TestLoader().loadTestsFromTestCase(Market)
    unittest.TextTestRunner(verbosity=2).run(suite)










