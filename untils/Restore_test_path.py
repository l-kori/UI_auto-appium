# coding=utf-8
from appium.webdriver.common.touch_action import TouchAction
import logging
import time


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='./log/hsl.log', level=logging.INFO, format=LOG_FORMAT)

def Restore(driver):
    while 1:
        el = driver.find_elements_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.LinearLayout[1]/android.widget.ImageView")
        if any(el):
            el1 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.LinearLayout[1]/android.widget.ImageView")
            el1.click()
            logging.info("已恢复到最初测试环境")
            break
        else:
            logging.info("未恢复到最初测试环境，继续恢复")
            driver.back()