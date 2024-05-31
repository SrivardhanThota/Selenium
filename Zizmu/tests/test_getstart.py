from selenium import webdriver
import time
from pages.getstart import Getstart
from .conftest import setup



class Test_Getstart:

    base_url = "https://zizmu.in/"
    name = "Srivardhan"
    email = "sri@gmail.com"
    contact = +919890000009
    massage = "Welcome to Zizmu Softwares"


    def test_getstart(self,setup):

        self.driver = setup
        self.driver.get(self.base_url)

        self.gt = Getstart(self.driver)
        self.gt.clickGetstart()
        self.gt.setName(self.name)
        time.sleep(2)
        self.gt.setEmail(self.email)
        time.sleep(2)
        self.gt.setContact(self.contact)
        time.sleep(2)
        self.gt.setMassage(self.massage)
        time.sleep(2)
        self.gt.clickSubmit()
        time.sleep(2)

