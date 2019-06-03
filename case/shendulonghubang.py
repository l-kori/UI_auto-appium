# coding=utf-8
import logging
import sys
sys.path.append('..')
from untils.Restore_test_path import *
from untils.sliding import *

def zhangtingyougu(device,driver):
    try:
        name = "涨停妖股"
        el1 = driver.find_element_by_id("com.hsl.stock:id/image_sdlhb")
        el1.click()
        el2 = driver.find_element_by_id("com.hsl.stock:id/txt_quote_title")
        el2.click()
        el2.click()
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

def longhubang(device,driver):
    try:
        name = "龙虎榜"
        el1 = driver.find_element_by_id("com.hsl.stock:id/image_sdlhb")
        el1.click()
        el2 = driver.find_element_by_id("com.hsl.stock:id/txt_demon_stock")
        el2.click()
        swipRight(driver)
        swipLeft(driver)
        el3 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]")
        el3.click()
        swipRight(driver)
        swipLeft(driver)
        el4 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]")
        el4.click()
        swipRight(driver)
        swipLeft(driver)
        el5 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[4]")
        el5.click()
        swipRight(driver)
        swipLeft(driver)
        el6 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[5]")
        el6.click()

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