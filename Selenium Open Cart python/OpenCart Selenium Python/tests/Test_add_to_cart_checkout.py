import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from pages.Add_to_cart_checkout import Add_to_cart_checkout
from pages.Login_to_cart import Login_to_cart


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

    # def test_login_to_cart(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.base_url)
    #     self.lgc = Login_to_cart(self.driver)
    #     self.lgc.home()
    #     self.lgc.setUserEmail(self.useremail)
    #     self.lgc.setPassword(self.password)
    #     self.lgc.login()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_to_cart_checkout(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lgc = Login_to_cart(self.driver)
        self.lgc.home()
        self.lgc.setUserEmail(self.useremail)
        self.lgc.setPassword(self.password)
        self.lgc.login()
        act_title == self.driver.title

        if act_title == "My Account":
            assert True
        else:
            assert False

        self.addcart = Add_to_cart_checkout(self.driver)
        time.sleep(2)
        self.addcart.setSearchbox(self.search)
        time.sleep(2)
        self.addcart.clickSearch()
        time.sleep(5)
        self.addcart.clickProduct()
        time.sleep(3)
        self.addcart.addtoCart()
        time.sleep(5)
        self.addcart.itemcheckout()
        time.sleep(2)
        self.addcart.checkOut()
        time.sleep(2)
        self.addcart.clickonNewcust()
        time.sleep(2)
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




