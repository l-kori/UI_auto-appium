# coding=utf-8
import time
from tomorrow import threads
from appium import webdriver
import sys
import os
sys.path.append('..')
from ..case.zhangtingqiangdu import *
from ..case.home_page_logo import *
from ..case.baozhangniugu import *
from ..case.shendulonghubang import *
from ..case.huanshoulv import *
@threads(3)
def run_case(device,driver):
    #首页所有logo
    logo(device,driver)
    # #涨停强度
    tab_zhangtingqiangdu(device,driver)
    #最强风口
    tab_zuiqiangfengkou(device,driver)
    #爆炒热度
    tab_baochaoredu(device,driver)
    #所有涨停板
    all_zhangtingban(device,driver)
    #自然版
    ziranban(device,driver)
    #一字板
    yiziban(device,driver)
    #涨停妖股
    zhangtingyougu(device,driver)
    #龙虎榜
    longhubang(device,driver)
    #换手率
    huanshoulv(device,driver)
    #多空博弈
    duokongboyi(device,driver)