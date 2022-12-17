import json

from jsonpath import jsonpath

class Utils:
    #:@classmethod可以用来为一个类创建一些预处理的实列
    @classmethod
    def jsonpath(cls,json_object,exper):
        return jsonpath(json_object,exper)