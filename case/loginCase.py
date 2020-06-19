#!usr/bin/env python3
# -*- coding:utf-8 _*-
import unittest

class TestMathMethod (unittest.TestCase):
# 两个正数相加
    def test_add_two_positive(self):
        res = 1
        print ("1+3的结果是{0}".format (res))
        try:
            self.assertEqual (5, res, "两个0相加的值不对！")  # 这里我为了可以报错，所以期望值写的是5
        except Exception as e:
            print("断言错误是{0}".format(e))
        raise e

        # 两个负数相乘
    def test_multi_two_negative(self):
        res = 1
        print ("-3*-9的结果是{0}".format (res))