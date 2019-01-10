# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/1/10 

import pytest

@pytest.mark.dong
@pytest.mark.P1
@pytest.mark.cm
class Test1(object):
    @pytest.mark.P1
    def test_1(self):
        print("this is test1")
        assert 1==1

    @pytest.mark.P0
    def test_2(selfs):
        print("this is test2")
        assert 1+2 ==3

@pytest.mark.mandy
@pytest.mark.P0
class Test2(object):
    def test_3(self):
        print("this is test3")
        assert  3+1 ==4

if __name__ =="__main__":
    pytest.main(["-s","demo_mark.py","-m=P0"])