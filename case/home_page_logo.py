# coding=utf-8
from tomorrow import threads
from appium.webdriver.common.touch_action import TouchAction
import logging
import time
from zhangtingqiangdu import *
import traceback
import sys
sys.path.append('..')
from untils.Restore_test_path import *


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='../log/hsl.log', level=logging.INFO, format=LOG_FORMAT)
def logo(device,driver):
    try:
        logging.info("设备："+device+"    目前测试内容：首页导航：涨停强度、暴涨牛股、自选股等")
        logging.info("设备："+device+"    遍历开始")
        el1 = driver.find_element_by_id("com.hsl.stock:id/image_zhangtingban")
        el1.click()
        # logging.info("设备："+device+"    点击涨停强度")
        driver.back()
        # logging.info("设备："+device+"    退出涨停强度")
        el2 = driver.find_element_by_id("com.hsl.stock:id/image_baozhangbankuai")
        el2.click()
        # logging.info("设备："+device+"    点击暴涨牛股")
        driver.back()
        # logging.info("设备："+device+"    退出暴涨牛股")
        el3 = driver.find_element_by_id("com.hsl.stock:id/image_sdlhb")
        el3.click()
        # logging.info("设备："+device+"    点击深度牛虎榜")
        driver.back()
        # logging.info("设备："+device+"    退出深度牛虎榜")
        el4 = driver.find_element_by_id("com.hsl.stock:id/image_huanshoulv")
        el4.click()
        # logging.info("设备："+device+"    点击换手率")
        driver.back()
        # logging.info("设备："+device+"    退出换手率")
        el5 = driver.find_element_by_id("com.hsl.stock:id/image_lurk_calendar")
        el5.click()
        # logging.info("设备："+device+"    点击潜伏日历")
        driver.back()
        # logging.info("设备："+device+"    退出潜伏日历")
        el6 = driver.find_element_by_id("com.hsl.stock:id/image_cixinzhuoyao")
        el6.click()
        # logging.info("设备："+device+"    点击次新捉妖")
        driver.back()
        # logging.info("设备："+device+"    退出次新捉妖")
        el7 = driver.find_element_by_id("com.hsl.stock:id/image_100")
        el7.click()
        # logging.info("设备："+device+"    点击100%中新股")
        driver.back()
        # logging.info("设备："+device+"退出100%中新股")
        el8 = driver.find_element_by_id("com.hsl.stock:id/image_duokongboyi")
        el8.click()
        # logging.info("设备："+device+"点击多空博弈")
        driver.back()
        # logging.info("设备："+device+"退出多空博弈")
        el9 = driver.find_element_by_id("com.hsl.stock:id/image_jihejingjia")
        el9.click()
        driver.back()

    except BaseException:
        logging.info("设备："+device+"    出现异常，记录问题日志！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
        logging.info("正在进行恢复测试环境")
        Restore(driver)
    else:
        logging.info("设备："+device+"测试结束，过程无异常")
        logging.info("正在进行恢复测试环境")
        Restore(driver)
