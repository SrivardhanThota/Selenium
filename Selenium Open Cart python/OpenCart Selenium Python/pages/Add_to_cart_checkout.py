import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.sanity

class Add_to_cart_checkout:

    txt_search_box_xpath = "//div[@id='search']/input"
    btn_search_xpath = "//button[@class='btn btn-light btn-lg']"
    product_hp_xpath = "//div[@class='image']//img[@title='HP LP3065']"
    btn_add_to_cart_xpath = "//button[contains(text(),'Add to Cart')]"
    btn_item_checkout_xpath = "//div[@class='dropdown d-grid']"
    btn_checkout_xpath = "//strong[normalize-space()='Checkout']//i[@class='fa-solid fa-share']"

    radio_newaddress_xpath = "//label[normalize-space()='I want to use a new address']"
    txt_box_firstname_id = "input-shipping-firstname"
    txt_box_lastname_id = "input-shipping-lastname"
    txt_box_address_id = "input-shipping-address-1"
    txt_box_city_id = "input-shipping-city"
    txt_box_postcode_id = "input-shipping-postcode"
    dropdown_country_id = "input-shipping-country"
    dropdown_state_id = "input-shipping-zone"
    btn_continue_xpath = "//button[@id='button-shipping-address']"

    def __init__(self,driver):
        self.driver = driver

    def home(self):
        self.driver.find_element(By.LINK_TEXT, "My Account").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()

    def setSearchbox(self,search):
        self.driver.find_element(By.XPATH,self.txt_search_box_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt_search_box_xpath).send_keys(search)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()

    def clickProduct(self):
        self.driver.find_element(By.XPATH,self.product_hp_xpath).click()

    def addtoCart(self):
        add = self.driver.find_element(By.XPATH,self.btn_add_to_cart_xpath)
        self.driver.execute_script("arguments[0].click();", add)

    def itemcheckout(self):
        self.driver.find_element(By.XPATH,self.btn_item_checkout_xpath).click()

    def checkOut(self):
        self.driver.find_element(By.XPATH,self.btn_checkout_xpath).click()

    def clickonNewcust(self):
        self.driver.find_element(By.XPATH,self.radio_newaddress_xpath).click()

    def setFirstname(self,firstname):
        self.driver.find_element(By.ID,self.txt_box_firstname_id).clear()
        self.driver.find_element(By.ID,self.txt_box_firstname_id).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element(By.ID,self.txt_box_lastname_id).clear()
        self.driver.find_element(By.ID,self.txt_box_lastname_id).send_keys(lastname)

    def setAddress(self,address):
        self.driver.find_element(By.ID,self.txt_box_address_id).clear()
        self.driver.find_element(By.ID,self.txt_box_address_id).send_keys(address)

    def setCity(self,city):
        self.driver.find_element(By.ID,self.txt_box_city_id).clear()
        self.driver.find_element(By.ID,self.txt_box_city_id).send_keys(city)

    def setPostcode(self,postcode):
        self.driver.find_element(By.ID,self.txt_box_postcode_id).clear()
        self.driver.find_element(By.ID,self.txt_box_postcode_id).send_keys(postcode)

    def setCountry(self):
        country = Select(self.driver.find_element(By.ID,self.dropdown_country_id))
        country.select_by_visible_text("India")

    def setState(self):
        state = Select(self.driver.find_element(By.ID,self.dropdown_state_id))
        state.select_by_visible_text("Telangana")

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_continue_xpath).click()








