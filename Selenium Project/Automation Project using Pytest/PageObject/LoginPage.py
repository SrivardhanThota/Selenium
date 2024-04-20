from selenium import webdriver
from selenium.webdriver.common.by import By
class Login:
    # textbox_username_id = "Email"
    # textbox_password_id = "Password"
    # button_login_xpath = "//button[@class='button-1 login-button']"
    # logout_link_text = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,"Email").clear()
        self.driver.find_element(By.ID,"Email").send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,"Password").clear()
        self.driver.find_element(By.ID,"Password").send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH,"//button[@class='button-1 login-button']").click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT,"Logout").click()