from selenium import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class BillingPage():

    def __init__(self, driver):
        self.driver = driver

        self.firstname_xpath_billing = "//input[@id='billing_first_name']"
        self.lastname_xpath_billing = "//input[@id='billing_last_name']"
        self.email_xpath_billing = "//input[@id='billing_email']"
        self.phone_xpath_billing = "//input[@id='billing_phone']"
        self.country_xpath_billing = "//span[@id='select2-chosen-1']"
        self.country_search_xpath_billing = "//input[@id='s2id_autogen1_search']"
        self.country_canada_xpath_billing   = "//span[@class='select2-match']"
        self.streetaddress_xpath_billing  = "//input[@id='billing_address_1']"
        self.townaddress_xpath_billing = "//input[@id='billing_city']"
        self.province_xpath_billing = "//span[@id='select2-chosen-2']"
        self.province_search_xpath_billing = "//input[@id='s2id_autogen2_search']"
        self.province_ontario_xpath_billing = "//span[@class='select2-match']"
        self.postalcode_xpath_billing = "//input[@id='billing_postcode']"
        self.payment_xpath_billing = "//input[@id='payment_method_cod']"
        self.placeorder_xpath_billing = "//input[@id='place_order']"

    def enter_firstname(self,firstname):
        self.driver.find_element_by_xpath(self.firstname_xpath_billing).send_keys(firstname)
    def enter_lastname(self,lastname):
        self.driver.find_element_by_xpath(self.lastname_xpath_billing).send_keys(lastname)

    def enter_Email(self,mail):
        self.driver.find_element_by_xpath(self.email_xpath_billing).send_keys(mail)
    def enter_phoneno(self,no):
        self.driver.find_element_by_xpath(self.phone_xpath_billing).send_keys(no)
    def enter_country(self,countryname):
        self.driver.find_element_by_xpath(self.country_xpath_billing).click()
        self.driver.find_element_by_xpath(self.country_search_xpath_billing).send_keys(countryname)
        self.driver.find_element_by_xpath(self.country_canada_xpath_billing).click()
    def enter_streetname(self,streetname):
        self.driver.find_element_by_xpath(self.streetaddress_xpath_billing).send_keys(streetname)
    def enter_townname(self,town):
        self.driver.find_element_by_xpath(self.townaddress_xpath_billing).send_keys(town)
    def select_province(self,province):
        self.driver.find_element_by_xpath(self.province_xpath_billing).click()
        self.driver.find_element_by_xpath(self.province_search_xpath_billing).send_keys(province)
        self.driver.find_element_by_xpath(self.province_ontario_xpath_billing).click()
    def enter_postalcode(self,postalcode):
        self.driver.find_element_by_xpath(self.postalcode_xpath_billing).send_keys(postalcode)
    def select_casondelivery(self):
        self.driver.find_element_by_xpath(self.payment_xpath_billing).click()
    def place_order(self):
        self.driver.find_element_by_xpath(self.placeorder_xpath_billing).click()



