# pytest_demo
pytest的demo

### pyDemo
该文件件主要是一些第三方插件的demo实践操作
- demo1.py 第一个demo
- demo_ordering.py 执行顺序
- demo_rerun.py  失败重跑
- demo_cov.py  覆盖率
- demo_fixture*.py  fixture相关

### 一些命令
生成html报告
```
pytest demo_fixture.py --html=./../report/report.html
```
重跑
```
pytest -sq demo_rerun.py --reruns 5  --reruns-delay 1
```
检查覆盖率
```
pytest --cov=../../xpinyin  demo_cov.py
```
