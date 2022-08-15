from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class  RegisterPage:
    def __init__(self, driver: WebDriver):
        self.drive = driver

    def register(self):
        username = "huangyanlan测试"
        manager_name = "huangyanlan测试"
        userphone = "13457656009"
        self.drive.find_element(By.ID, "corp_name").send_keys(username)
        self.drive.find_element(By.ID, "manager_name").send_keys(manager_name)
        self.driver.find_element(By.ID, "register_tel").send_keys("13457656009")
        self.driver.find_element(By.ID, "submit_btn").click()
        return True