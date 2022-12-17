def traverslist(self, list_str: list):
    lists = ""
    if list_str is None:
        lists = lists + "{}"
        return lists
    else:
        list_str = list_str.sort()
        lists = lists + "["
        print("看舒服可以进来{}".format(list_str))
        for item in list_str:
            if isinstance(item, dict):
                lists = lists + str(self.traversMap(item))
            elif isinstance(item, list):
                lists = lists + str(self.traverslist(item))
            else:
                lists = lists + str(item)
            lists = lists + ","

        return lists