from selenium import webdriver
from selenium.webdriver.common.by import By


class Register:

    textbox_firstname_id = "input-firstname"
    textbox_lastname_id = "input-lastname"
    textbox_email_id = "input-email"
    textbox_password_id = "input-password"
    subscribe_checkbox_xpath = "//input[@id='input-newsletter']"
    privacy_checkbox_xpath = "//input[@name='agree']"
    continue_btn_xpath = "//button[normalize-space()='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def home(self):
        self.driver.find_element(By.LINK_TEXT, "My Account").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).clear()
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).clear()
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lastname)

    def setEmail(self, email):
        self.driver.find_element(By.ID,self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def Subscribe(self):
        self.driver.find_element(By.XPATH, self.subscribe_checkbox_xpath).click()

    def Privacy(self):
        self.driver.find_element(By.XPATH, self.privacy_checkbox_xpath).click()
        # self.driver.execute_script("arguments[0].click();", privacy)
    def Continue_btn(self):
        self.driver.find_element(By.XPATH, self.continue_btn_xpath).click()