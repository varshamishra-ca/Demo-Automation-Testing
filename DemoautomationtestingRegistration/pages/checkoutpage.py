from selenium import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.checkout_xpath = "//a[@class='checkout-button button alt wc-forward']"

    def click_checkout(self):
        self.driver.find_element_by_xpath(self.checkout_xpath).click()
