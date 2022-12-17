l = []
class keyvalue():

    def print_keyvalue_all(self, input_json):
        key_value = ''
        if isinstance(input_json, dict):
            for key in input_json.keys():
                # print(key)
                key_value = input_json.get(key)
                # print(key_value)
                if isinstance(key_value, dict):
                    self.print_keyvalue_all(key_value)
                # elif isinstance(key_value, list):
                #     for json_array in key_value:
                #      self.print_keyvalue_all(json_array)
                else:
                    l.append(str(key) + "=" + str(key_value))
                    print("这是存入的列表{}".format(l))
                    print(str(key) + "=" + str(key_value))
        elif isinstance(input_json, list):
             for input_json_array in input_json:
                self.print_keyvalue_all(input_json_array)

        return l

if __name__ == '__main__':
    input_json = {
        "param": {"a": "11", "b": "22", "c": "33"},
        "token": "",
        "deviceId": "",
        "d_track_data": {"session_id": "gfgfgfgfgfgfgfggfgfgfg", "project": "主小程序", "tdc": "", "tpc": "",
                         "uuid": "bgbgbgbgbgbgbgbgbgbg", "env": "minip"},
        "dfdf": ["fdh","ewe","huahau"]
    }
    s = keyvalue().print_keyvalue_all(input_json)
    print("最后生成的列表{}".format(s))
    print("&".join(s))