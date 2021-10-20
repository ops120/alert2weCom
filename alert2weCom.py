from flask import request
from flask import Flask
import urllib.request
import json

app = Flask(__name__)

url = "https://qyapi.weixin.qq.com"
token = "自己申请企微的Token"


@app.route("/webhook", methods=['POST'])
def message():

    des = request.json.get("message").strip()
    title = request.json.get("ruleName").strip()
    state = request.json.get("state").strip()     #增加告警状态
    values = {
     "msgtype": "news",
     "news": {
        "articles" : [
            {
                "title" : title + "[" + state +"]",   #增加告警状态
                "description" : des,
                "url" : "需要进行发送的link",
                "picurl" : "需要进行发送的图片link"
            }
         ]
    }
}
    msges=(bytes(json.dumps(values), 'utf-8'))
    send_url = '%s/cgi-bin/webhook/send?key=%s' % (url,token)
    respone=urllib.request.urlopen(urllib.request.Request(url=send_url, data=msges)).read()

    return respone


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 9988)
