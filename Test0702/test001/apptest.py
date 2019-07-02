# -*- coding:utf-8 -*-
from appium import webdriver
import time

# app连接配置信息
conf = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.FreshAir",
    "appActivity": ".activity.WelcomeActivity",
    "noReset": "true",
    "unicodeKeyboard": "true",
    "resetKeyboard": "true"
}
# 通过remote方法连接appium方法连接
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", conf)

# 设置隐式等待10s

driver.implicitly_wait(10)
# 登录
# 输入手机号码
ele = driver.find_element_by_id('com.FreshAir:id/login_by_pwd_phone')
ele.clear()
ele.send_keys('15316039123')
# 输入密码
ele = driver.find_element_by_id('com.FreshAir:id/login_by_pwd')
ele.clear()
ele.send_keys('123456')
# 点击登录
ele = driver.find_element_by_id('com.FreshAir:id/login_by_pwd_login')
ele.click()

# 退出app
ele = driver.find_element_by_id('com.FreshAir:id/main_menu')
ele.click()

ele = driver.find_element_by_id('com.FreshAir:id/menu_left_user_icon')
ele.click()

ele = driver.find_element_by_id('com.FreshAir:id/fm_phone_quite')
ele.click()

ele = driver.find_element_by_id('android:id/button1')
ele.click()

# time.sleep(4)

driver.quit()
