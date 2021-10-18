# alert2weCom
grafana使用原生webhook调用企微发送告警，不需进行任何改造，史上最简实现方式

1.服务器环境准备:
Centos >= 7.0  或windows 需要安装python3

2.安装pip:
yum install -y python-pip

3.安装flask:
pip3 install flask

4.copy 代码至本地

5.执行代码 python3 alert2weCom.py

6.grafana 配置webhook 即可发送告警

关于 Grafana ALert功能使用webhook 教程直接搜索即可。
