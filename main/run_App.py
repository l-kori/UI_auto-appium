# coding=utf-8
import time
from tomorrow import threads
from appium import webdriver
import logging
import run_case
@threads(1)
def run_app(device,port):
    time.sleep(2)
    capabilities = {
        "platformName": "Android",
        "deviceName": device,
        "appPackage": "com.hsl.stock",
        "appActivity": "com.hsl.stock.module.main.StartV2Activity",
        "newCommandTimeout": "3000",
        "noReset": True
    }
    logging.info("APP启动")
    driver =  webdriver.Remote('http://0.0.0.0:' + str(port) + '/wd/hub', capabilities)
    time.sleep(5)

    #启动APP
    run_case.run_case(device,driver)