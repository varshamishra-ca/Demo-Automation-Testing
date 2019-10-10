from selenium import *


class LandingPage():

    def __init__(self, driver):
        self.driver = driver

        self.email_xpath="//input[@id='email']"
        self.enter_xpath ="//img[@id='enterimg']"
        self.skipsignin_xpath = "//button[@id='btn2']"

    def enter_email(self,email):
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)

    def enter(self):
        self.driver.find_element_by_xpath(self.enter_xpath).click()
    def skipsignin(self):
        self.driver.find_element_by_xpath(self.skipsignin_xpath).click()



