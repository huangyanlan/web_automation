from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Web import logingPage
from Web import RegisterPage


class IndexPage:
    def __init__(self):
        # options = Options()
        # options.debugger_address('127.0.0.1:9222')
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return logingPage(self.driver)

    def goto_register(self):
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return RegisterPage(self.driver)