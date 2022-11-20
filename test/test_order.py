import pytest


class TestOrder():
    @pytest.mark.run(order=1)
    def test_wownow(self):
        print("进入wownow首页")

    @pytest.mark.run(order=2)
    def test_takeway(self):
        print("进入外卖首页")
    @pytest.mark.last
    def test_search(self):
        print("搜索")

    @pytest.mark.run(order=4)
    def test_nearby(self):
        print("附近门店")

    @pytest.mark.run(order=3)
    def test_top(self):
        print("主题曲广告")