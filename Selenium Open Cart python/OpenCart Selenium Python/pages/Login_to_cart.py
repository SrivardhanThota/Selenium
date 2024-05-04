from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_to_cart:

    textbox_email_id = "input-email"
    textbox_password_id = "input-password"
    btn_login_xpath = "//button[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def home(self):
        self.driver.find_element(By.LINK_TEXT, "My Account").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()

    def setUserEmail(self, useremail):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(useremail)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
        assert self.driver.find_element(By.LINK_TEXT,"My Account").is_displayed()
