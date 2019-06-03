# coding=utf-8
from tomorrow import threads
from appium.webdriver.common.touch_action import TouchAction
import logging
import time
import home_page_logo
import sys
sys.path.append('..')
from untils.Restore_test_path import *
from untils.sliding import *

def all_zhangtingban(device,driver):
    try:
        name = "全部涨停板"
        logging.info("设备：" + device + "    开始执行" + name)
        el1 = driver.find_element_by_id("com.hsl.stock:id/image_baozhangbankuai")
        el1.click()
        el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout")
        el2.click()
        el2.click()
        swipRight(driver)
        swipLeft(driver)
        el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout")
        el3.click()
        el3.click()
        swipRight(driver)
        swipLeft(driver)
        logging.info("设备：" + device + "    执行完毕，" + name + "未出现崩溃")
    except BaseException:
        if is_activity_started("com.hsl.stock", device):
            logging.info("设备：" + device + " " + name + "   出现异常，记录问题日志！！！！！！！！！！！！！！！")
            logging.info("正在进行恢复测试环境")
            Restore(driver)
        else:
            logging.info("设备：" + device + " " + name + "   出现奔溃异常，记录问题日志！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
    else:
        logging.info("设备：" + device + "" + name + "测试结束，过程无异常")
        logging.info("正在进行恢复测试环境")
        Restore(driver)

def ziranban(device,driver):
    try:
        name = "自然板"
        logging.info("设备：" + device + "    开始执行" + name)
        el1 = driver.find_element_by_id("com.hsl.stock:id/image_baozhangbankuai")
        el1.click()
        el2 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
        el2.click()
        el3 = driver.find_element_by_id("com.hsl.stock:id/txt_quote_title")
        el3.click()
        el3.click()
        swipRight(driver)
        swipLeft(driver)
        el4 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView")
        el4.click()
        el4.click()
        swipRight(driver)
        swipLeft(driver)
        logging.info("设备：" + device + "    执行完毕，" + name + "未出现崩溃")
    except BaseException:
        if is_activity_started("com.hsl.stock", device):
            logging.info("设备：" + device + " " + name + "   出现异常，记录问题日志！！！！！！！！！！！！！！！")
            logging.info("正在进行恢复测试环境")
            Restore(driver)
        else:
            logging.info("设备：" + device + " " + name + "   出现奔溃异常，记录问题日志！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
    else:
        logging.info("设备：" + device + "" + name + "测试结束，过程无异常")
        logging.info("正在进行恢复测试环境")
        Restore(driver)

def yiziban(device,driver):
    try:
        name = "一字板"
        logging.info("设备：" + device + "    开始执行" + name)
        el1 = driver.find_element_by_id("com.hsl.stock:id/image_baozhangbankuai")
        el1.click()
        el2 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
        el2.click()
        el8 = driver.find_element_by_id("com.hsl.stock:id/txt_quote_title")
        el8.click()
        el8.click()
        swipRight(driver)
        swipLeft(driver)
        el9 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView")
        el9.click()
        el9.click()
        swipRight(driver)
        swipLeft(driver)
        logging.info("设备：" + device + "    执行完毕，" + name + "未出现崩溃")
    except BaseException:
        if is_activity_started("com.hsl.stock", device):
            logging.info("设备：" + device + " " + name + "   出现异常，记录问题日志！！！！！！！！！！！！！！！")
            logging.info("正在进行恢复测试环境")
            Restore(driver)
        else:
            logging.info("设备：" + device + " " + name + "   出现奔溃异常，记录问题日志！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
    else:
        logging.info("设备：" + device + "" + name + "测试结束，过程无异常")
        logging.info("正在进行恢复测试环境")
        Restore(driver)