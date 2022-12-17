#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
import operator

s = ['chu','shu','jin']
# 用-去连接列表中每个元素
d = {
    "param":{"a":"11","b":"22","c":"33"},
    "token":"",
    "deviceId":"",
     "d_track_data":{"session_id":"gfgfgfgfgfgfgfggfgfgfg","project":"主小程序","tdc":"","tpc":"","uuid":"bgbgbgbgbgbgbgbgbgbg","env":"minip"}
}
# print(d.items())

#存记录最后列表：
list_last =[]

class datajson:

    def get_datajson(self,d):
        l = []
        global s
        # data = dict(sorted(d.items(), key=operator.itemgetter(0)))
        for key,value in d.items():
            print("这是key值{}".format(key))
            print("这是value值{}".format(value))
            if isinstance(value, dict):
                global dictlen
                dictlen=len(value)
                print("这是字典值{}".format(dictlen))
                self.get_datajson(value)
                print("牛逼")
                dict_last_str=str(key)+"={"+s+"}"
                print(str(key)+"={"+s+"}")
                list_last.append(dict_last_str)
            elif isinstance(value, list):
                last_list2=[]
                for value_list in value:
                    if isinstance(value_list, dict):
                        # global dictlen
                        # dictlen = len(value)
                        # self.get_datajson(value_list)
                        s=self.s(value_list)
                        dict_last_str = str(key) + "={" + s + "}"
                        print(str(key) + "={" + s + "}")
                        last_list2.append(dict_last_str)
                    else:
                        print(str(key) + "=" + str(value))
                        last_list2.append(str(key) + "=" + str(value))
                        # list_last.append(last_list_str)
                        break
                last_list2.sort()
                new_str_list="&".join(last_list2)

                print("优秀{}".format(new_str_list))
                list_last.append(new_str_list)
                # print(str(key) + "=" + str(last_list2))
            else:
                print(str(key) + "=" + str(value))
                l.append(str(key) + "=" + str(value))
                l.sort()
                s = "&".join(l)
                # print("新字典{}".format(dictlen))
                # if j == dictlen:
                #     print("长度相同")
                #     return s
                # return s
        return "这是转换后的{}".format(list_last)

    def s(self,value):
        if value is None:
            lists = value + "{}"
            return lists
        else:
            dicts = dict(sorted(value.items(), key=operator.itemgetter(0)))
            for key, value in dicts.items():
                s=self.get_datajson(value)
                dict_last_str = str(key) + "={" + s + "}"
                print(str(key) + "={" + s + "}")
                print("循环list值:{}".format(lists))
            return lists
    def l(self,value):
        pass

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
    s = datajson().get_datajson(input_json)
    print("最后生成的列表{}".format(s))
    # print("&".join(s))
#print("=".join(i))
# print(str(d))
# # print(d.items())
# # #------------输出-----------------
# #
# requstbody = ["&".join(i) for i in d.items()]
#
# print(requstbody)
#
#print("&".join(requstbody))