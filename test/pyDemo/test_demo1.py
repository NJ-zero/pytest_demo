# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/1/8 

import pytest
import random


'''
pip install pytest-assume  ---多重校验 multiple failures per test
'''


def add(x,y):
    return x+y

class TestAdd():

    def test_add1(self):
        assert add(2,3)==5
        assert add(1,3)==3
        assert add(2,5)==7

    def test_add2(self):
        pytest.assume(add(1,2)==3)
        pytest.assume(add(1,4)==3)
        pytest.assume(add(2,2)==4)

    num=[(1+2,3),(2+2,4),(3*3,9)]
    @pytest.mark.parametrize("x,y",num)
    def test_add3(self,x,y):
        assert x==y

