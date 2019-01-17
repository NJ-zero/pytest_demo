# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/1/10 

'''
pip3 install pytest-allure-adaptor

然后安装allure-commandline
'''

import allure
import pytest

@allure.story('story_1')
@allure.severity('normal')
@allure.step("描述")
def test_add():
    '''
    判断两个是否相等
    '''
    assert 1==1

allure.environment(app_package='com.qukan.kdd')
allure.environment(app_activity='com.qukan.kdd.activity')
allure.environment(device_name='huawei')
allure.environment(platform_name='Android')
