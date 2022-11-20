import yaml


def setup_module():
    print("模块级别初始化")

def teardown_module():
    print("模块级别结束")
def setup_function():
    print("函数开始")

def teardown_function():
    print("函数结束")

def test_s():
        print("函数拉拉")
class Test_pytest1:
    def setup_class(self):
        print("类开始")

    def teardown_class(self):
        print("类结束结束")
    def setup(self):
        print("方法开始")

    def teardown(self):
        print("方法结束")
    def test_yaml(self):
        print(yaml.safe_load(open("datas.yml")))

    def test_y(self):
        print("方法2")
class Test_pytest2:
    def test_2(self):
        print("多个类")