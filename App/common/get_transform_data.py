#--encoding='utf-8'--
import base64

from App.common.getRequestData import RequestJson
import hashlib
import hmac
import datetime
class TransformDate:

    def get_sign(self, deviceid, requesttm, data):
        if not bool(data):
            return "deviceId=" + deviceid + "&" + "requestTm=" + requesttm
        elif len(data)==0:
            return "deviceId="+deviceid+"&"+"requestTm="+requesttm
        else:

            requestlist = RequestJson().get_request_transform(data)
            print("调用函数生成的列表：{}".format(requestlist))
            # if requestlist
            requestlist.append("deviceId="+deviceid)
            requestlist.append("requestTm="+requesttm)
            requestlist.sort()
            str_sign="&".join(requestlist)
            print("ffdf:{}".format(str_sign))
            sign = self.MD5_demo(str_sign)
            print("sign:{}".format(sign))
            return sign
    def MD5_demo(sefl,s):

      md= hashlib.md5()# 创建md5对象
      # md.digest()
      md.update(s.encode())

      return md.hexdigest()
      # 签名MD5+base64



if __name__ == '__main__':
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
    print("requests数据类型:{}".format(type(data)))
    retuesttm ='20221128003127'
    deviceid = "12345"
    transform_str = TransformDate().get_sign(deviceid, retuesttm,data)
    # s ='businessScope=&deviceId=12345&isNew=false&location={lat=23.120011&lon=113.401101}&marketingTypes=[]&pageNum=1&pageSize=4&requestTm=20221128003127&sortType='
    # transform_str=TransformDate().MD5_demo(s)
    print("打印出最后转换的字符串：{}".format(transform_str))