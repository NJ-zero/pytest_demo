# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/1/10 

import pytest

@pytest.fixture(scope="session",autouse="True")
def before():
    print("this is conftest")