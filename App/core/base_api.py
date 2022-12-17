import yaml

from App.utils.utils import Utils
import requests
import json as complexjson
from App.common.logger import logger
class BaseApi:
    # json_data = None
    # api_root_url = get_datas()

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def jsonpath(self,exper):
        return Utils.jsonpath(self.json_data, exper)

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, headers=None, data=None, **kwargs):
        return self.request(url, "POST", headers, data, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, url, method,headers, data=None, **kwargs):
        url = self.api_root_url + url
        # headers = dict(**kwargs).get("headers")
        # params = dict(**kwargs).get("params")
        # files = dict(**kwargs).get("params")
        # cookies = dict(**kwargs).get("params")
        self.request_log(url, method, headers, data)
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return requests.post(url=url, headers=headers, data=data, **kwargs)
        # if method == "PUT":
        #     if json:
        #         # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
        #         data = complexjson.dumps(json)
        #     return self.session.put(url, data, **kwargs)
        # if method == "DELETE":
        #     return self.session.delete(url, **kwargs)
        # if method == "PATCH":
        #     if json:
        #         data = complexjson.dumps(json)
        #     return self.session.patch(url, data, **kwargs)

    def request_log(self, url, method, headers=None,data=None,**kwargs):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
