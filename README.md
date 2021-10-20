# alert2weCom
grafana使用原生webhook调用企微发送告警，不需进行任何改造，史上最简实现方式

1.服务器环境准备:
Centos >= 7.0  或windows 需要安装python3

2.安装pip:
yum install -y python-pip

3.安装flask:
pip3 install flask

4.copy 代码至本地,无脑下载也可

5.执行代码 python3 alert2weCom.py

6.grafana 配置webhook 即可发送告警

关于 Grafana ALert功能使用webhook 教程直接搜索即可。

企微告警示例：

postman测试代码

![image](https://github.com/ops120/alert2weCom/blob/main/postman%E6%B5%8B%E8%AF%95.png)


企微显示的结果标例：

![image](https://github.com/ops120/alert2weCom/blob/main/%E4%BC%81%E5%BE%AE%E5%91%8A%E8%AD%A6%E7%A4%BA%E4%BE%8B.png)
