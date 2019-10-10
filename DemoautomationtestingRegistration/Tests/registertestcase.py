
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
            #register.click_language()
            #driver.find_element_by_xpath("//div[@id='msdd']").click()
            #time.sleep(10)
            #driver.find_element_by_xpath("//a[contains(text(),'English')]").click()
            #register.click_language()

            #driver.find_element_by_xpath("//div[@class='container center']//div[contains(@class,'row')]").click()
            #register.click_skills()
            register.select_country()

            register.select_year()
            register.select_month()
            register.select_day()
            register.enter_password("Abcd1234")
            register.enter_second_password("Abcd1234")
            register.enter_submit()
            time.sleep(3)
            driver.get_screenshot_as_file("/Users/sumit/Desktop/CACC Barsha/DemoautomationtestingRegistration/screenshots/regisgister.png")


    @classmethod
    def tearDownClass(cls):
        print("close")
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/sumit/Desktop/CACC Barsha/DemoautomationtestingRegistration/reports/RegReports"))







