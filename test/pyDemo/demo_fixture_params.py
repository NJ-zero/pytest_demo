# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/1/9 

import pytest
import json

test_user_data = [{"user": "admin1", "passwd": "111111"},
                  {"user": "admin1", "passwd": ""}]

@pytest.fixture(scope="module",params=test_user_data)
def login(request):
    return request.param

def test_login(login):
    print(login["user"])
