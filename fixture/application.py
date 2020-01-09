from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self):
        self.driver = Firefox()
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()