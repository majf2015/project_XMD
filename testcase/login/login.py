# -*- coding: utf-8 -*-
from selenium import webdriver
import time

class Login:
    def __init__(self):
        self.url = 'http://192.168.1.100:9880/spa-manager/login'
        self.user_name = u'曲奇'
        self.pass_wd = 'a123456'
        self.browser = webdriver.Chrome()

    def login(self):
        self.browser.get(self.url)
        self.browser.find_element_by_id('user-name').send_keys(self.user_name)
        self.browser.find_element_by_id('user-pw').send_keys(self.pass_wd)
        self.browser.find_element_by_xpath("//input[@value= '立即登录']").click()
        time.sleep(5)


    def write_off_coupon(self):
        self.browser.find_element_by_xpath("//input").send_keys('106341781024')
        self.browser.find_element_by_xpath("//div[@class = 'use-all-row']/a[1]").click()

l = Login()
l.login()
l.write_off_coupon()


