from selenium import webdriver
from selenium.webdriver.common.by import By



class Getstart:

    btn_gtstart_xpath = "//button[@id='getStartedButton']"
    plc_name_xpath = "(//input[@id='name'])[1]"
    plc_email_xpath = "(//input[@id='email'])[1]"
    plc_contact_xpath = "(//input[@id='contactNumber'])[1]"
    plc_massage_xpath = "(//textarea[@id='message'])[1]"
    btn_submit_xpath = "(//button[@type='submit'][text()='Submit'])[1]"


    def __init__(self,driver):
        self.driver = driver

    def clickGetstart(self):
        self.driver.find_element(By.XPATH,self.btn_gtstart_xpath).click()

    def setName(self,name):
        self.driver.find_element(By.XPATH,self.plc_name_xpath).clear()
        self.driver.find_element(By.XPATH,self.plc_name_xpath).send_keys(name)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.plc_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.plc_email_xpath).send_keys(email)

    def setContact(self,contact):
        self.driver.find_element(By.XPATH, self.plc_contact_xpath).clear()
        self.driver.find_element(By.XPATH, self.plc_contact_xpath).send_keys(contact)

    def setMassage(self,massage):
        self.driver.find_element(By.XPATH, self.plc_massage_xpath).clear()
        self.driver.find_element(By.XPATH, self.plc_massage_xpath).send_keys(massage)

    def clickSubmit(self):
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()



