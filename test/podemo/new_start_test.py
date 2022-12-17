import operator


class SuperAppsingnatrue:
    def sign(self,data):
        data= dict(sorted(data.items(),key=operator.itemgetter(0)))
        print("按字母从小到大排序后的字典{}".format(data))
        lists =""
        if data is not None:
            for key,value in data.items():
                self.traverse(lists,key,value)

        return lists

    def traverse(self,lists,key,value):
        l = []
        if isinstance(value, dict):
            print("新的value值{}".format(value))
            lists=lists+str(key)+"="+str(self.traversMap(value))+"&"
            print("第一次打印list:{}".format(lists))
        elif isinstance(value, list):
            lists = lists + str(key) + "=" + str(self.traverslist(value)) + "&"
            print("第二次打印list:{}".format(lists))
        else:
            # lists=lists+str(key) + "="+str(value)+"&"
            print(str(key) + "=" + str(value))
            l.append(str(key) + "=" + str(value))
            l.sort()
            s = "&".join(l)
            print("第三次打印list:{}".format(s))
    def traversMap(self,dicts):
        global l
        l = []
        lists=""
        if dicts is None:
            lists = lists + "{}"
            return lists
        else:
            lists="{"
            dicts=dict(sorted(dicts.items(), key=operator.itemgetter(0)))
            for key,value in dicts.items():
                list=lists+str(self.traverse(lists, key, value))
                print("循环list值:{}".format(lists))
            return lists
    def traverslist(self,list_str:list):
        l = []
        global lists
        lists =""
        if list_str is None:
            lists = lists + "{}"
            return lists
        else:
            print(list_str)
            # list_str.sort()
            lists=lists+"["
            print("看舒服可以进来{}".format(list_str))
            for item in list_str:
                if isinstance(item, dict):
                    lists=lists+str(self.traversMap(item))
                elif isinstance(item, list):
                    lists = lists + str(self.traverslist(item))
                else:
                    lists = lists + str(item)
                lists=lists+","

            return lists


if __name__ == '__main__':
    input_json = {
        "hylqfy":"1314",
        "param": {"a": "11", "b": "22", "c": "33"},
        "token": "",
        "deviceId": "",
        "d_track_data": {"session_id": "gfgfgfgfgfgfgfggfgfgfg", "project": "主小程序", "tdc": "", "tpc": "",
                         "uuid": "bgbgbgbgbgbgbgbgbgbg", "env": "minip"},
        "dfdf": ["fdh","ewe","huahau"],
        "paramse":{
            "missyou":"哈哈哈哈",
            "active":["3234","3234"],
            "dadd":"1234343443"
        },
        "params": [{
            "comd":"23244",
            "shootid":"432323"
        },
            {
                "comd": "9999",
                "shootid": "6666"
            },
        ]
    }
    sign_last=SuperAppsingnatrue().sign(input_json)
    print("最后打印{}".format(sign_last))