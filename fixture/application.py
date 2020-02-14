from selenium import webdriver
#from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        #self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        driver = self.driver
        if not (driver.current_url.endswith("addressbook/") and len(driver.find_elements_by_css_selector("[value='Send e-Mail']")) > 0):
            driver.get(self.base_url)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()