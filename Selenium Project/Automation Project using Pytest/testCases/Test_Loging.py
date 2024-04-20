import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
import pytest
from PageObject.LoginPage import Login

class Test_001_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # username = "admin@yourstore.com"
    # password = "admin"

    def test_homepagetitle(self,setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        act_title = self.driver.title
        self.driver.close()

        if act_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        self.lp = Login(self.driver)
        self.lp.setUserName("admin@yourstore.com")
        time.sleep(2)
        self.lp.setPassword("admin")
        self.lp.login()
        time.sleep(3)
        act_title = self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
        else:
            assert False