# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/1/16

import pytest
import allure
import random

class TestDemo2(object):
    @allure.story('story_2')
    @pytest.mark.flaky(reruns=6, reruns_delay=1)
    def test_cm(self):
        assert 2==random.randint(0,3)

@allure.feature('feature_2')
@allure.story('story_2')
@allure.severity('minor')
class TestDemo2_1(object):
    def test_pd(self):
        assert 2==2