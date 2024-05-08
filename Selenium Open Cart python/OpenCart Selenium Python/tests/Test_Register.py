from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random
import pytest
from datetime import datetime
from pages.Register import Register
from utilities.customLogger import LogGen
# from .conftest import setup

class Test_Register:

    url = "http://localhost/opencart/upload/index.php?route=account/register&language=en-gb"
    firstname = "Thota"
    lastname = "Sreevardhan"
    password = "Thota@7680"
    email = "srivardhanthota.maroli@gmail.com"
    logger = LogGen.loggen()
    def test_register_with_mandatory_fiels(self,setup):
        self.logger.info("******Registering******")
        self.driver = setup
        self.driver.get(self.url)
        self.rg = Register(self.driver)
        self.rg.home()
        self.rg.setFirstName(self.firstname)
        self.rg.setLastName(self.lastname)
        # self.email = random_email_generator() + "@gmail.com"
        self.rg.setEmail(self.email)
        self.rg.setPassword(self.password)
        time.sleep(3)
        self.rg.Subscribe()
        time.sleep(3)
        self.rg.Privacy()
        time.sleep(5)
        self.rg.Continue_btn()


def random_email_generator(self,size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))