#--encoding='utf-8'--
import requests
import json
from App.core.result_base import ResultBase
from App.api.home import home_request
from App.common.logger import logger


from App.common.get_transform_data import TransformDate
from App.core.base_api import BaseApi

import datetime
import time
def get_merch():
    result = ResultBase()
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
            "pageNum": 1

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
    res = home_request.near_merch(headers=he,data=da)
    result.success = False
    if res.json()["rspCd"] == "00000":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["rspCd"], res.json()["rspInf"])
    result.msg = res.json()["rspInf"]
    result.response = res
    logger.info("查询附近门店 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
    # print("返回数据是：{}".format(respoen))
    # r = self.request(method='post',url=url,headers=he,data=da)
    # respoen = requests.post(url=url,headers=he,data=da)


