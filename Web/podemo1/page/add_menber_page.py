
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Web.podemo1.page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AddMemberPage(BasePage):

    def add_menber(self, name, acount, phone):
        self.driver.find_element(By.ID, "username").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(acount)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_operationBar.ww_operationBar:nth-child(1) a:nth-child(2)").click()
        return True

    def get_menber(self, usename):

        total_list = []
        while True:
            sleep(5)
            contactlist = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            titlelist = [element.get_attribute("title") for element in contactlist]
            print(titlelist)
            total_list = total_list+titlelist
            if usename in total_list:
                return total_list
            result: str = self.driver.find_element(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            print(result)
            num, total = result.split('/', 1)
            if int(num) == int(total):
                break

            else:
                self.driver.find_element(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()
        # while True:
        #     sleep(5)
        #     contactlist = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        #     titlelist = [element.get_attribute("title") for element in contactlist]
        #     print(titlelist)
        #     total_list = total_list + titlelist
        #     if usename in total_list:
        #         return total_list
        #     result: str = self.driver.find_element(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
        #     print(result)
        #     num, total = result.split('/', 1)
        #
        #     if int(num) == int(total):
        #         break
        #     else:
        #         self.driver.find_element(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()
        return total_list
