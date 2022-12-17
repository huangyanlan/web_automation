#--encoding='utf-8'--
import requests
import json

import yaml

from App.common.get_transform_data import TransformDate

import datetime
import time

class PageMode:
    def get_merch(self):
        url = "https://appgateway-uat.lifekh.com/gateway_web/takeaway-merchant/app/super-app/nearby"
        data = {
            "marketingTypes": [],
            "sortType": "",
            "pageSize": "4",
            "businessScope": "",
            "location": {
                "lat": 23.120011,
                "lon": 113.401101
            },
            "isNew": "false",
            "pageNum": "1"

        }
        print("data数据类型:{}".format(type(data)))
        locatiem = str(time.localtime())
        time_stamp = str(time.mktime(time.localtime()))
        retuesttm = time_stamp[0:len(time_stamp)-2]
        deviceid = "python"
        sign = TransformDate().get_sign(deviceid, retuesttm, data)
        he ={
            "appVersion": "3.0",
            "requestTm": retuesttm,
            "appId": "SuperApp",
            "channel": "app store",
            "sign": sign,
            "appno": "11",
            "termTyp": "IOS",
            "projectName": "SuperApp",
            "deviceId": deviceid,
            'Content-Type': 'application/json;charset=utf-8',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept': 'application/json, text/plain, */*',
            'signver': '1.0',
            'Accept-Language': 'zh-CN'
        }
        print("请求头的签名数据类型:{}".format(he["sign"]))
        print("请求的签名数据类型:{}".format(type(json.dumps(data))))
        print("请求时间:{}".format(retuesttm))
        print(time_stamp)
        da=json.dumps(data,ensure_ascii=False)
        respoen = requests.post(url=url,headers=he,data=da)
        print("请求体是：{}".format(type(respoen.request.body)))

        return respoen

if __name__ == '__main__':
	re = PageMode().get_merch()
	print("打印出响应数据：{}".format(re.json()))

with open("../config/config_uat.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        print(f"读取的环境数据：{datas['http.host.appgateway']}")
        f.close()
