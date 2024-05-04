import time

from selenium import webdriver
from pages.Login_to_cart import Login_to_cart



class Test_Login_to_Cart:

    base_url = "http://localhost/opencart/upload/index.php?route=common/home&language=en-gb"
    useremail = "srivardhanthota.marolix@gmail.com"
    password = "Thota@7680"

    def test_login_to_cart(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lgc = Login_to_cart(self.driver)
        self.lgc.home()
        self.lgc.setUserEmail(self.useremail)
        self.lgc.setPassword(self.password)
        self.lgc.login()
        time.sleep(3)

        self.driver.close()


