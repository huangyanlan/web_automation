#--encoding='utf-8'--
import requests
import json
import os

from App.common.get_transform_data import TransformDate
from App.core.base_api import BaseApi
import yaml

import datetime

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "config_uat.yaml")
# api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]
with open(data_file_path, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    f.close()
    api_root_url=datas['http.host.appgateway']

class home_request(BaseApi):
    def __init__(self, api_root_url, **kwargs):
        super(home_request, self).__init__(api_root_url, **kwargs)
    def near_merch(self,**kwargs):
        return self.post("/gateway_web/takeaway-merchant/app/super-app/nearby", **kwargs)




home_request = home_request(api_root_url)