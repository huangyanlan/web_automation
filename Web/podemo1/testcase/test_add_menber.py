import string

import pytest
import yaml
import random
import time

from Web.podemo1.page.main_page import MainPage


def get_datas():
    with open("./datas/datas_wx.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        print(datas)
        f.close()
    return datas
# 随机生成单个手机号
def get_mobile():
    mobiles = ["134","139"]
    numbers = "".join(random.sample(string.digits, 8))
    mobile = random.choice(mobiles)+numbers
    return mobile
# 批量生成多个手机号，并写入txt文档
def get_mobiles():
    phonelist =[]
    while True:
     mobiles = ["134","139"]
     numbers = "".join(random.sample(string.digits, 8))
     mobile = random.choice(mobiles)+numbers
     phonelist.append(mobile)
     with open("./datas/phone.txt", 'a') as f:
         f.write(mobile+'\n')

     if len(phonelist) == 10:
         f.close()
         break

class TestAdd:

    def setup(self):
        self.main = MainPage()
        datas = get_datas()
        phone = get_mobile()
        print(get_mobile())
        get_mobiles()
    @pytest.mark.parametrize("name,acount,phone", [(get_mobile(),get_mobile(),get_mobile())])
    def test_add_success(self, name, acount, phone):
        # name = random.randint()
        # acount = "03355iep"
        # phone =
        addmenber = self.main.goto_add()
        addmenber.add_menber(name, acount, phone)
        usename:str = name
        listtile = addmenber.get_menber(usename)

        assert usename in listtile