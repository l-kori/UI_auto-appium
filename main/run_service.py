# coding=utf-8
import time
from tomorrow import threads
from appium import webdriver
import random
import os
from multiprocessing import Process
import logging
import run_App
import sys
sys.path.append('..')
from case.home_page_logo import logo
from untils.if_collapse import *


@threads(3)
def run_devices():
    # 读取设备 id
    readDeviceId = list(os.popen('adb devices').readlines())
    len1 = len(readDeviceId)
    len2 = len1 - 2
    del readDeviceId[0]
    del readDeviceId[len2]
    # 当前设备数
    readDeviceId_num = len(readDeviceId)
    if readDeviceId_num != 0:
        logging.info('当前设备数:' + str(len(readDeviceId)))
        # print "当前设备数" + len(readDeviceId)
        for i in readDeviceId:
            port = random.randint(2000, 2300)
            rr = i.split("\t")
            p = Process(target=run_appium, args=(port, rr[0],))
            # 服务器启动
            p.start()
            logging.info("appium服务启动")
            # APP启动
            run_App.run_app(rr[0],port)
            time.sleep(10)

    else:
        logging.info("当前没有可启动的Android手机，请检查设备连接")

def run_appium(port,devices):
    cmd = "appium -a 127.0.0.1 -p "+str(port)+" -U "+devices+""
    os.system(cmd)