# coding=utf-8
import time
from appium import webdriver
import logging
from main import run_case
from case import loginCase
from untils import reportHtml

def run_app(device,port):
    time.sleep(2)
    capabilities = {
        "platformName": "Android",
        "deviceName": device,
        "appPackage": "com.songheng.eastnews",
        "appActivity": "com.oa.eastfirst.activity.WelcomeActivity",
        "newCommandTimeout": "3000",
        "noReset": True
    }
    logging.info("APP启动")
    driver = webdriver.Remote('http://0.0.0.0:' + str(port) + '/wd/hub', capabilities)
    time.sleep(5)

    #执行测试用例
    run_case.run_test_case()