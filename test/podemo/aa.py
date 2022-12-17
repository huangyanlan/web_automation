
class RequestJson:

    def get_request_transform(self, d):
        #每次递归调用都会初始化存储转换数据的列表
        l = []
        # print("用add函数有什么效果：{}".format(sr))
        for key,value in d.items():
            if isinstance(value, dict):
                s=self.get_request_transform(value)
                # s = "&".join(s)
                dict_last_str = str(key) + "={" + "&".join(s) + "}"
                l.append(dict_last_str)
            elif isinstance(value, list):
                # 存
                ss=""
                # 当值是列表时，设置一个空列表将，存入列表遍历的数据
                list_value=[]
                for value_list in value:
                    if isinstance(value_list, dict):
                        s=self.get_request_transform(value_list)
                        # s = "&".join(s)
                        dict_last_str = "{" + "&".join(s) + "}"
                        ss=ss+dict_last_str+","

                        # list_value.append(dict_last_str)
                    else:
                        ss = ss+value_list+","
                        # list_value.append(value_list)
                ss = ss[0:len(ss)-1]+"]"
                # print("拼接后的字符串：{}".format(ss))
                # list_value.append(ss)
                # s=str(key)+"="+str(list_value)
                s = str(key) + "=[" + ss
                l.append(s)

            else:
                l.append(str(key) + "=" + str(value))
        # l.append("deviceid=" + re)
        # l.append("requestTm=" + tm)
        l.sort()
        # print("最后的list:{}".format(s))
        print("最后的l:{}".format(l))
        #请求拼接后，最后生成的数据
        return l


if __name__ == '__main__':
    input_json = {
        "hylqfy": "1314",
        "param": {"a": "11", "b": "22", "c": "33"},
        "token": "",
        "deviceId": "",
        "d_track_data": {"session_id": "gfgfgfgfgfgfgfggfgfgfg", "project": "主小程序", "tdc": "", "tpc": "",
                         "uuid": "bgbgbgbgbgbgbgbgbgbg", "env": "minip"},
        "dfdf": ["fdh","ewe","huahau"],
        "operatorNo": {
            "missyou":"哈哈哈哈",
            "active":["3234","3234"],
            "dadd":"1234343443"
        },
        "businessScope": [{
            "comd":"23244",
            "shootid":"432323"
        },
            {
                "comd": "9999",
                "shootid": "6666"
            },
            "898"
        ],
        "username":[],
        "appuser":{}
    }
    re="520520"
    tm="666666"
    s = RequestJson().get_request_transform(input_json)
    print("转换后的数据:-->{}".format(s))