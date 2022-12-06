# _*_ coding:utf-8 _*_
import sys
import os
import unittest
import time

# 找到根目录
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加进根目录
sys.path.append(root_path)


from Python_HTMLTestReportCN import HTMLTestReportCN

report_path = os.path.join(root_path, 'test_report')
now_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

HtmlFile = os.path.join(report_path, now_time + "-test.html")


if __name__ == '__main__':
    with open(HtmlFile, 'wb') as file:
        print(os.path.abspath(__file__))
        suites = unittest.TestLoader().discover(
            os.path.join(root_path, 'test_suites'))
        runner = HTMLTestReportCN.HTMLTestRunner(
            stream=file,
            title='Api_Auto_Test测试报告',
            description=u'执行情况',
            tester='junliangl',
        )
        runner.run(suites)
