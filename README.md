# pytest_demo
pytest的demo

### pyDemo
该文件件主要是一些第三方插件的demo实践操作
- test_demo1.py 第一个demo
- test_ordering.py 执行顺序
- test_rerun.py  失败重跑
- test_cov.py  覆盖率
- test_fixture*.py  fixture相关
- test_mark  自定义标签

### report
该文件主要存放报告
- report.html 是 html报告
- html/xml 是allure生成的report
### 一些命令
生成html报告
```
pytest test_fixture.py --html=./../report/report.html
```
重跑
```
pytest -sq test_rerun.py --reruns 5  --reruns-delay 1
```
检查覆盖率
```
pytest --cov=../../xpinyin  test_cov.py
```
执行指定测试用例
```
pytest -sq -k 2 demo_mark.py

pytest -sq -m "P0" demo_mark.py

pytest -sq demo_fixture_decorator.py::Test2::test_3
```
allure report相关
```
pytest -s -q ./  --alluredir=../report/xml
allure generate ../report/xml  -o ../report/hmtl --clean
生成最终html文件
```
