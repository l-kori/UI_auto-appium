# coding=utf-8
from case import loginCase
from untils.reportHtml import *
def run_test_case():
    #一个run等于执行一个测试集，输出一个报告
    runCaseReportHtml(loginCase)