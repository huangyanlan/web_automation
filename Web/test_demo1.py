from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo1:
    def setup_method(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    # def test_demo1(self):
    #     self.driver.get("https://www.baidu.com/")
    #     sleep(3)

    def test_weixin(self):
        self.driver.find_element(By.XPATH, "//ul[@class='main-menu-list']//li[3]").click()
        sleep(6)
        self.driver.find_element(By.XPATH, "//div[@class='el-scrollbar__view']/div[3]").click()
        sleep(3)
        self.driver.find_element(By.XPATH, "//div[@class='el-scrollbar__view']/div[3]/ul/span[4]").click()
        sleep(3)
    # def test_cookic(self):
    #     # cookies = self.driver.get_cookies()
    #     # print(cookies)
    #     cookies = [{'domain':'.work.weixin.qq.com','httpOnly':True,'name':'wwrtx.logined','path':'/','secure':False,'value':'true'},{'domain':'.work.weixin.qq.com','httpOnly':False,'name':'wwrtx.cs_ind','path':'/','secure':False,'value':''},{'domain':'.work.weixin.qq.com','httpOnly':False,'name':'wxpay.vid','path':'/','secure':False,'value':'1688853097024424'},{'domain':'.work.weixin.qq.com','httpOnly':False,'name':'wxpay.corpid','path':'/','secure':False,'value':'1970325031172040'},{'domain':'.work.weixin.qq.com','httpOnly':False,'name':'wwrtx.vid','path':'/','secure':False,'value':'1688853097024424'},{'domain':'.qq.com','expiry':2147385600,'httpOnly':False,'name':'pgv_pvid','path':'/','secure':False,'value':'1505384053'},{'domain':'.work.weixin.qq.com','httpOnly':True,'name':'wwrtx.ref','path':'/','secure':False,'value':'direct'},{'domain':'.work.weixin.qq.com','httpOnly':True,'name':'wwrtx.ltype','path':'/','secure':False,'value':'1'},{'domain':'.work.weixin.qq.com','httpOnly':False,'name':'wwrtx.d2st','path':'/','secure':False,'value':'a9971207'},{'domain':'.work.weixin.qq.com','httpOnly':True,'name':'wwrtx.refid','path':'/','secure':False,'value':'35552983651804867'},{'domain':'.work.weixin.qq.com','httpOnly':True,'name':'wwrtx.sid','path':'/','secure':False,'value':'kfCYjTrXONVB8hL1jJuKfxXbdGTS2q_4teuU1ivNGL1jm3d3QZE1C5Ojc6l8exZm'},{'domain':'.work.weixin.qq.com','expiry':1688273283,'httpOnly':False,'name':'wwrtx.c_gdpr','path':'/','secure':False,'value':'0'},{'domain':'.work.weixin.qq.com','httpOnly':True,'name':'wwrtx.vst','path':'/','secure':False,'value':'3uRK0XJLnPz3JasOJglOpIAiZ9SYHjku2YY9B3-F1rZnt7GUME6LeWt94Q4QSkZxSBMZWdoV6tpyMw5o0wd3S33RRV13u8F6Hpg6YQxJGtNCrIaFjp-DA0wGHpe59tCB0X_QT-prhh7TLAZYfQ_NE2KqbGCYQP1K0V2YKVrrzxMbSYkCJs4MF_dO0HMLTqRm84ng0oUCUZL7aPnASQ0unIT8ZJnwkjmMh_EXRRRHDd1gZMMPPmwqBuEmGIR7xQ0Byzx8__L7i7zdvx7gy3le9w'},{'domain':'.work.weixin.qq.com','expiry':1659346313,'httpOnly':False,'name':'wwrtx.i18n_lan','path':'/','secure':False,'value':'zh'}]
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
    #     # sleep(10)
    #     for cookie in cookies:
    #         self.driver.add_cookie(cookie)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
    #     sleep(3)
