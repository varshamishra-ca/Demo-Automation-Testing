from selenium import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Homepage():

    def __init__(self, driver):
        self.driver = driver

        self.search_xpath="//i[@class='icon-search']"
        self.search_type_xpath = "//input[@id='s']"
        self.select_seleniumruby_xpath ="//h3[contains(text(),'Selenium Ruby')]"

    def click_search(self):
        self.driver.find_element_by_xpath(self.search_xpath).click()
    def type_java(self,value):
        self.driver.find_element_by_xpath(self.search_type_xpath).send_keys(value)
    def select_seleniumruby(self):
        self.driver.find_element_by_xpath(self.select_seleniumruby_xpath).click()