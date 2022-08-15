from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from Web.podemo1.page.add_menber_page import AddMemberPage
from Web.podemo1.page.base_page import BasePage


class  MainPage(BasePage):

    def goto_add(self):
        #进入联系人页
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
        sleep(10)
        #点击添加联系人
        #self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar:nth-child(1) a:nth-child(2)").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")
        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, "username")
            except:
                return False
        WebDriverWait(self.driver, 10).until(wait_for_next)  # 一直等到username元素
        return AddMemberPage(self.driver)