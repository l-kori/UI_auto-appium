#!usr/bin/env python3
# -*- coding:utf-8 _*-
import unittest
import time
from main import run_service

class TestMathMethod (unittest.TestCase):
    # 初始化app
    def setUp(self):
        self.driver = run_service.run_devices()

    # 执行  退出登录case
    def test01(self):
        # 点击我的
        self.driver.find_element_by_id("com.songheng.eastnews:id/a_q").click()
        # 点击我的设置
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.TextView").click()
       # 点击
        self.driver.find_element_by_id("com.songheng.eastnews:id/ec").click()
        # 加入隐式等待，等待弹框出现
        self.driver.implicitly_wait(3)
        #确认退出
        self.driver.find_element_by_id("com.songheng.eastnews:id/ahw").click()