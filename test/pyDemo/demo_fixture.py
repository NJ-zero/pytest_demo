# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/1/9 

'''
函数名直接调用fixture
'''

import pytest

@pytest.fixture()
def pre():
    print("beore test ")
    yield
    print("after test")

class Test1(object):

    def test_1(self,pre):
        print("tihs is test1")
        assert 1==1

    def test_2(selfs):
        print("this is test2")
        assert 1+2 ==3

if __name__=="__main__":
    pytest.main(['-q','demo_fixture.py'])