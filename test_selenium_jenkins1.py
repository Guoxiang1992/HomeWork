# -- coding: utf-8 --
# @File : test_selenium_jenkins.py
import allure
import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.feature("持续集成测试百度demo")
class TestBaidu:
    def setup(self):
        #判断是否有use_headless这个环境变量如果有就
        try:
            use_headless=os.environ['headless']
        except:
            use_headless=None
        if use_headless == 1:
            opt=webdriver.ChromeOptions()
            opt.add_argument('headless')#不打开浏览器运行,--headless也可以一样的效果
            self.driver= webdriver.Chrome(options=opt)
        else:
            self.driver=webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    @allure.story("测试百度搜索海贼王")
    def test_baidu(self):
        with allure.step("打开百度网页"):
            self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.ID, 'kw').send_keys('海贼王')
        self.driver.find_element(By.ID, 'su').click()
        time.sleep(3) #等待页面加载完成再去断言
        assert "海贼王" in self.driver.title

    @allure.story("测试百度搜索火影忍者")
    def test_baidu1(self):
        with allure.step("打开百度网页"):
            self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.ID, 'kw').send_keys('火影忍者')
        self.driver.find_element(By.ID, 'su').click()
        time.sleep(3)  # 等待页面加载完成再去断言
        assert "火影忍者" in self.driver.title