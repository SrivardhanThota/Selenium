import time
from .conftest import *
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from pages.Add_to_cart_checkout import Add_to_cart_checkout
from pages.Login_to_cart import Login_to_cart
from utilities.customLogger import LogGen

@pytest.mark.regression
class Test_to_add_to_cart_checkout:

    base_url = "http://localhost/opencart/upload/index.php?route=common/home&language=en-gb"
    useremail = "srivardhanthota.marolix@gmail.com"
    password = "Thota@7680"
    search = "hp"
    firstname = "Thota"
    lastname = "Srivardhan"
    address = "hyderabad"
    city = "Hyderabad"
    postcode = "12345"
    # country = "India"
    # state = "Telangana"

    logger = LogGen.loggen()

    # def test_login_to_cart(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.base_url)
    #     self.lgc = Login_to_cart(self.driver)
    #     self.lgc.home()
    #     self.lgc.setUserEmail(self.useremail)
    #     self.lgc.setPassword(self.password)
    #     self.lgc.login()

    @pytest.mark.sanity

    def test_add_to_cart_checkout(self,setup):
        self.logger.info("*********Verify the Addto cart checkout********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lgc = Login_to_cart(self.driver)
        self.lgc.home()
        self.lgc.setUserEmail(self.useremail)
        self.lgc.setPassword(self.password)
        self.lgc.login()
        time.sleep(3)
        # act_title == self.driver.title
        # time.sleep(3)
        # if act_title == "My Account":
        #     assert True
        # else:
        #     assert False
        self.logger.info("*********Performing the action********")
        self.addcart = Add_to_cart_checkout(self.driver)
        time.sleep(2)
        self.addcart.setSearchbox(self.search)
        time.sleep(2)
        self.addcart.clickSearch()
        time.sleep(2)
        self.addcart.clickProduct()
        time.sleep(3)
        self.addcart.addtoCart()
        time.sleep(5)
        self.addcart.itemcheckout()
        time.sleep(3)
        self.addcart.checkOut()
        time.sleep(2)
        self.addcart.clickonNewcust()
        time.sleep(3)
        self.addcart.setFirstname(self.firstname)
        # time.sleep(2)
        self.addcart.setLastname(self.lastname)
        # time.sleep(2)
        self.addcart.setAddress(self.address)
        # time.sleep(2)
        self.addcart.setCity(self.city)
        # time.sleep(2)
        self.addcart.setPostcode(self.postcode)
        # time.sleep(2)
        self.addcart.setCountry()
        time.sleep(3)
        self.addcart.setState()
        time.sleep(3)
        self.addcart.clickContinue()
        time.sleep(2)
        self.addcart.clickChooseShipping()
        time.sleep(2)
        self.addcart.clickradio()
        time.sleep(2)
        self.addcart.continueclick()
        time.sleep(2)
        self.addcart.choosepayment()
        time.sleep(2)
        self.addcart.cashondelivery()
        time.sleep(3)
        self.addcart.continuecashondelivery()
        time.sleep(2)
        self.addcart.confirmorder()
        time.sleep(2)







