# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/1/9 

'''
装饰器调用fixture
'''

import pytest

@pytest.fixture()
def pre():
    print("beore test ")
    yield
    print("after test")

class Test1(object):

    @pytest.mark.usefixtures('pre')
    def test_1(self):
        print("this is test1")
        assert 1==1

    def test_2(selfs,pre):
        print("this is test2")
        assert 1+2 ==3

class Test2(object):
    def test_3(self):
        print("this is test3")
        assert  3+1 ==4