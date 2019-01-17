# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/1/16 

import pytest
import allure
import random

class TestDemo3(object):

    @pytest.mark.flaky(reruns=6, reruns_delay=1)
    def test_cm(self):
        assert 2==random.randint(0,3)


class TestDemo2_1(object):
    @allure.severity('critical')
    def test_pd(self):
        assert 3==3