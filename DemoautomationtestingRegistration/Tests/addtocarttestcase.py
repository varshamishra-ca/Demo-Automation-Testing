from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
import unittest
import time
from selenium.webdriver.support.ui import Select


from pages.landingPage import LandingPage
from pages.registrationPage import RegistrationPage
from pages.homepage import Homepage
from pages.productpage import Productpage
from pages.checkoutpage import CheckoutPage
from pages.billingpage import BillingPage

class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Chrome(executable_path ="/Users/sumit/Desktop/CACC Barsha/DemoautomationtestingRegistration/drivers/chromedriver")
        cls.driver.implicitly_wait(5)

    def test_register(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in/")
        titleoflandingPage = driver.title
        print(titleoflandingPage)

        land = LandingPage(driver)
        land.enter_email("sweetycacc@gmail.com")
        land.enter()
        time.sleep(10)
        register = RegistrationPage(driver)
        register.enter_firstname("Barsha")
        register.enter_lasttname("Mishra")
        register.enter_address("135 Luella cres, Brampton")
        register.enter_emailaddress("sweetycacc@gmail.com")
        register.enter_phonenumber("6472893375")
        register.select_gender()
        register.select_hobby()
        register.select_country()
        register.select_year()
        register.select_month()
        register.select_day()
        register.enter_password("Abcd1234")
        register.enter_second_password("Abcd1234")
        register.enter_submit()
        time.sleep(3)
        driver.get_screenshot_as_file("/Users/sumit/Desktop/CACC Barsha/DemoautomationtestingRegistration/screenshots/regisgister.png")

    def test_addtocart(self):
            driver = self.driver

            driver.get("http://demo.automationtesting.in/")
            titleoflandingPage = driver.title
            print(titleoflandingPage)
            land = LandingPage(driver)
            land.skipsignin()
            registerpage = driver.title
            print(registerpage)
            self.assertNotEqual(titleoflandingPage,registerpage,"page didnt change")
            time.sleep(5)
            practice = RegistrationPage(driver)
            practice.click_practicetest()
            time.sleep(5)
            practicesite =driver.title
            print(practicesite)
            self.assertEqual("Automation Practice Site",practicesite,"Both title matches")
            x= Homepage(driver)
            x.select_seleniumruby()
            y =Productpage(driver)
            y.click_add()
            driver.get_screenshot_as_file("/Users/sumit/Desktop/CACC Barsha/DemoautomationtestingRegistration/screenshots/addtocart.png")
            c =Productpage(driver)
            c.click_cart()
            co =CheckoutPage(driver)
            co.click_checkout()
            b =BillingPage(driver)
            b.enter_firstname("Brish")
            b.enter_lastname("Cool")
            b.enter_Email("sweetycacc@gmail.com")
            b.enter_phoneno("6758972345")
            b.enter_country("Canada")
            b.enter_streetname("167 luella cres")
            b.enter_townname("Brampton")
            b.select_province("Ontario")
            #driver.find_element_by_xpath("//span[@id='select2-chosen-2']").click()
            b.enter_postalcode("l7a3h9")
            b.select_casondelivery()
            time.sleep(5)
            b.place_order()
            time.sleep(10)
            driver.get_screenshot_as_file("/Users/sumit/Desktop/CACC Barsha/DemoautomationtestingRegistration/screenshots/Orderplaced.png")





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/sumit/Desktop/CACC Barsha/DemoautomationtestingRegistration/screenshots/addtocart"))