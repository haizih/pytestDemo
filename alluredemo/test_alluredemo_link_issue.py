# -*- coding: UTF-8 -*-
# Filename:test_alluredemo_link_issue.py
# Author: duke
# Date: 2020-12-09 17:31
import allure
@allure.link("http://www.baidu.com", name='链接')  #name可加可不加，不加直接展示链接
def test_with_link():
    print('这是一条加了链接的测试')
    pass

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issures/8#issuecomment-268313637'
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_testcase_link():
    print('这是一条测试用例的链接，链接到测试用例里面')
    pass

# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue('140','这是一个issue')
def test_with_issue_link():
    pass
