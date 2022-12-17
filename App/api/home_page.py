#--encoding='utf-8'--
import requests
import json


from App.common.get_transform_data import TransformDate
from App.core.base_api import BaseApi

import datetime
import time
class PageMode(BaseApi):
    def get_merch(self, pageNum):
        url = "/gateway_web/takeaway-merchant/app/super-app/nearby"
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
            "pageNum": pageNum

        }
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
        da=json.dumps(data,ensure_ascii=False)
        # respoen=BaseApi().post(url,he,da)
        respoen = self.post(url, he, da)
        # print("返回数据是：{}".format(respoen))
        # r = self.request(method='post',url=url,headers=he,data=da)
        # respoen = requests.post(url=url,headers=he,data=da)

        return respoen

if __name__ == '__main__':
	re = PageMode().get_merch(2)
	print("打印出响应数据：{}".format(re.json()))

