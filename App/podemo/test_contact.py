from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "DQLRJVLJCEPBCEUG"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = True
        #不停止应用，直接运行测试用例
        # caps["dontStopAppOnReset"]= True
        caps["skipDeviceInitialization"] = True
        caps["skipServerInstallation"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
    def test_contact(self):
        username="huangyl986"
        phone = '13457678768'
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0))').click()
        #self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(username)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@class='android.widget.EditText']").send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()


