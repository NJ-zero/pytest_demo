# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/1/9

'''
pip install pytest-cov   覆盖率

执行命令
pytest --cov=../../xpinyin  demo_cov.py

'''


from xpinyin import Pinyin
import pytest

pin = Pinyin()
@pytest.mark.parametrize("hanyu,pinyin",[
    ("你好","ni-hao"),
    ("上海","shang-hai"),
])
def test_pin1(hanyu,pinyin):
    print(1)
    assert pin.get_pinyin(hanyu)==pinyin
    assert pin.get_pinyin()=="ni-hao"
    assert pin.get_pinyin("上海", tone_marks='numbers',convert='upper') =="SHANG4-HAI3"
    assert pin.get_pinyin("上海", tone_marks='numbers', convert='capitalize') == "Shang4-Hai3"
    assert pin.get_pinyin("上海", tone_marks='numbers') == "shang4-hai3"
    assert pin.get_pinyin("上海", tone_marks='marks', convert='capitalize') == "Shàng-Hǎi"
    assert pin.get_pinyin("上海", tone_marks='marks',) == "shàng-hǎi"
    assert pin.get_pinyin("上海", tone_marks='marks',convert='upper') == "SHÀNG-HǍI"

def test_initial():
    print(2)
    pytest.assume(pin.get_initial("哈") == "H")
    pytest.assume(pin.get_initial() == "N")
    pytest.assume(pin.get_initial("N") == "N")

def test_get_initials():
    print(3)
    assert pin.get_initials("上海") =="S-H"
    assert pin.get_initials("S-H") == "S---H"
    assert pin.get_initials() == "N-H"
    assert pin.get_initials("上海","") == "SH"
    assert pin.get_initials("SH", "") == "SH"
    assert pin.get_initials("上海"," ") == "S H"
    assert pin.get_initials("SHD", " ") == "S H D"

