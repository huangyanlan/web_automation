from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class logingPage:

    def __init__(self,driver: WebDriver):
        self.drive = driver


    def scan(self):
        pass

    def goto_register(self):
        self.drive.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return