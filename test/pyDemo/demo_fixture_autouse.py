# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/1/9 

'''
autouse 调用fixture
'''

import pytest

@pytest.fixture(scope="class",autouse=True)
def preclass():
    print("beore class ")
    yield
    print("after class")

@pytest.fixture(scope="module",autouse=True)
def premodule():
    print("beore module ")
    yield
    print("after module")

@pytest.fixture(scope="function",autouse=True)
def pretest():
    print("beore function ")
    yield
    print("after function")

class Test1(object):

    def test_1(self):
        print("this is test1")
        assert 1==1

    def test_2(self):
        print("this is test2")
        assert 1+2 ==3

class Test2(object):
    def test_3(self):
        print("this is test3")
        assert  3+1 ==4

    def test_4(self):
        print("this is test4")
        assert  3+2 ==5