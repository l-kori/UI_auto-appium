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
from untils.if_collapse import *

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='../log/hsl.log', level=logging.INFO, format=LOG_FORMAT)


def tab_zhangtingqiangdu(device, driver):
    try:
        name = "涨停强度"
        logging.info("设备：" + device + "    开始执行" + name + "")
        el1 = driver.find_element_by_id("com.hsl.stock:id/image_zhangtingban")
        el1.click()
        el2 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
        el2.click()
        el3 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
        el3.click()
        el4 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
        el4.click()
        el5 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[4]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
        el5.click()
        el5.click()
        el6 = driver.find_element_by_id("com.hsl.stock:id/tv_limitUp")
        el6.click()
        el7 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView")
        el7.click()
        el7.click()
        el8 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView")
        el8.click()
        el8.click()
        el9 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
        el9.click()
        el10 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout")
        el10.click()
        el10.click()
        el11 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView")
        el11.click()
        el11.click()
        el12 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
        el12.click()
        el13 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout")
        el13.click()
        el13.click()
        el14 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView")
        el14.click()
        el14.click()
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


def tab_zuiqiangfengkou(device, driver):
    try:
        name = "最强风口"
        logging.info("设备：" + device + "    开始执行" + name + "")
        el1 = driver.find_element_by_id("com.hsl.stock:id/image_zhangtingban")
        el1.click()
        el2 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.LinearLayout[2]/android.widget.TextView")
        el2.click()
        el3 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]")
        el3.click()
        el4 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]")
        el4.click()
        el5 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]")
        el5.click()
        el6 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView")
        el6.click()
        el6.click()
        el7 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView")
        el7.click()
        el7.click()
        el8 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]")
        el8.click()
        el8.click()
        el9 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout")
        el9.click()
        el10 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout")
        el10.click()
        el10.click()
        el11 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]")
        el11.click()
        el12 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView")
        el12.click()
        el12.click()
        el13 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView")
        el13.click()
        el13.click()
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


def tab_baochaoredu(device, driver):
    name = "爆炒热度"
    try:
        logging.info("设备：" + device + "    开始执行" + name)
        el1 = driver.find_element_by_id("com.hsl.stock:id/image_zhangtingban")
        el1.click()
        el2 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.LinearLayout[3]/android.widget.TextView")
        el2.click()
        el3 = driver.find_element_by_id("com.hsl.stock:id/radio_H1")
        el3.click()
        el4 = driver.find_element_by_id("com.hsl.stock:id/radio_H2")
        el4.click()
        el5 = driver.find_element_by_id("com.hsl.stock:id/radio_H3")
        el5.click()
        el6 = driver.find_element_by_id("com.hsl.stock:id/button")
        el6.click()
        el7 = driver.find_element_by_id("com.hsl.stock:id/image_back")
        el7.click()
        el8 = driver.find_element_by_id("com.hsl.stock:id/tvST")
        el8.click()

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