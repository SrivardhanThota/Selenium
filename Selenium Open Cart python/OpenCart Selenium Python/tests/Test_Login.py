import time

from selenium import webdriver
from .conftest import setup
from pages.Login import Login
from utilities.customLogger import LogGen

class Test_Login:

    base_url = "http://localhost/opencart/upload/admin/index.php?route=common/login"
    username = "admin"
    password = "admin"

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lg = Login(self.driver)
        self.lg.setUserName(self.username)
        self.lg.setPassword(self.password)
        self.lg.login()
        time.sleep(3)

        # act_title = self.driver.title
        # if act_title =="My Account":
        #     assert True
        # else:
        #     assert False

        self.driver.close()
