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
                    else:
                        ss = ss+value_list+","
                ss = ss[0:len(ss)-1]+"]"
                s = str(key) + "=[" + ss
                l.append(s)

            else:
                l.append(str(key) + "=" + str(value))
        # l.append("deviceid=" + re)
        # l.append("requestTm=" + tm)
        l.sort()
        # print("最后的list:{}".format(s))
        #请求拼接后，最后生成的数据
        return l
