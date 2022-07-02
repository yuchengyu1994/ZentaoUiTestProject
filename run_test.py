import HTMLTestRunner
import os
import time
import unittest

current_path=os.path.dirname(__file__)
report_path=os.path.join(current_path,'test_report')
case_path=os.path.join(current_path,'test_cases')
html_path=os.path.join(report_path,'result%s.html'%(time.strftime('%Y-%m-%d-%H-%M-%S')))
discover= unittest.defaultTestLoader.discover(start_dir=case_path,pattern='*_case.py',top_level_dir=case_path)
suite=unittest.TestSuite()
suite.addTest(discover)
file=open(html_path,'wb')
html_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='禅道UI自动化项目',
                                            description='由自动化测试完成')
html_runner.run(suite)