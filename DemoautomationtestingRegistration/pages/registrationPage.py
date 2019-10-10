from selenium import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class RegistrationPage():

    def __init__(self, driver):
        self.driver = driver

        self.firstname_xpath="//input[@placeholder='First Name']"
        self.lastname_xpath ="//input[@placeholder='Last Name']"
        self.address_xpath = "//textarea[@class='form-control ng-pristine ng-untouched ng-valid']"
        self.emailsaddress_xpath  ="//input[@type='email']"
        self.phonenumber_xpath = "//input[@type='tel']"
        self.gender_female_xpath = "//label[2]//input[1]"
        self.hobbies_cricket_xpath = "//input[@id='checkbox1']"
        self.languages_xpath = "//div[@id='msdd']"
        self.languages_english_xpath = "//a[contains(text(),'English')]"
        self.skill_xpath = "//div[@class='container center']//div[contains(@class,'row')]"
        self.country_xpath = "//select[@id='countries']"
        self.year_xpath = "//select[@id='yearbox']"
        self.month_xpath ="//select[@placeholder='Month']"
        self.day_xpath = "//select[@id='daybox']"
        self.firstpassword_xpath  = "//input[@id='firstpassword']"
        self.scndpassword_xpath = "//input[@id='secondpassword']"
        self.submit_xpath = "//button[@id='submitbtn']"
        self.practicetest_xpath = "//a[contains(text(),'Practice Site')]"

    def enter_firstname(self,firstname):
        self.driver.find_element_by_xpath(self.firstname_xpath).send_keys(firstname)

    def enter_lasttname(self,lasttname):
        self.driver.find_element_by_xpath(self.lastname_xpath).send_keys(lasttname)
    def enter_address(self,address):
        self.driver.find_element_by_xpath(self.address_xpath).send_keys(address)
    def enter_emailaddress(self,email):
        self.driver.find_element_by_xpath(self.emailsaddress_xpath).send_keys(email)
    def enter_phonenumber(self,phnumber):
        self.driver.find_element_by_xpath(self.phonenumber_xpath).send_keys(phnumber)
    def select_gender(self):
         self.driver.find_element_by_xpath(self.gender_female_xpath).click()


    def select_hobby(self):
        self.driver.find_element_by_xpath(self.hobbies_cricket_xpath).click()

    def click_language(self):
        self.driver.find_element_by_xpath("//div[@id='msdd']").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//a[contains(text(),'English')]").click()
        self.driver.implicitly_wait(5)

    def click_english_language(self):
        self.driver.find_element_by_xpath(self.languages_english_xpath).click()

    def click_skills(self):
        self.driver.find_element_by_xpath(self.skill_xpath).click()
    def select_country(self):
        countryelement = self.driver.find_element_by_xpath(self.country_xpath)
        canada = Select(countryelement)
        canada.select_by_index("42")

    def select_year(self):
        yearelement = self.driver.find_element_by_xpath(self.year_xpath)
        year= Select(yearelement)
        year.select_by_visible_text("1987")
    def select_month(self):
        monthelement = self.driver.find_element_by_xpath(self.month_xpath)
        month= Select(monthelement)
        month.select_by_visible_text("July")

    def select_day(self):
        dayelement = self.driver.find_element_by_xpath(self.day_xpath)
        day= Select(dayelement)
        day.select_by_visible_text("12")
    def enter_password(self,pwd):
        self.driver.find_element_by_xpath(self.firstpassword_xpath).send_keys(pwd)
    def enter_second_password(self,pwd):
        self.driver.find_element_by_xpath(self.scndpassword_xpath).send_keys(pwd)
    def enter_submit(self):
        self.driver.find_element_by_xpath(self.submit_xpath).click()
    def click_practicetest(self):
        self.driver.find_element_by_xpath(self.practicetest_xpath).click()












