from selenium import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Productpage():

    def __init__(self, driver):
        self.driver = driver

        self.addtocart_xpath = "//button[@class='single_add_to_cart_button button alt']"
        self.cart_xpath= "//span[@class='cartcontents']"

    def click_add(self):
        self.driver.find_element_by_xpath(self.addtocart_xpath).click()

    def click_cart(self):
        self.driver.find_element_by_xpath(self.cart_xpath).click()