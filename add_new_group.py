# -*- coding: utf-8 -*-
from selenium import webdriver
from group import Group
import unittest

class add_new_group(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_add_new_group(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_group(driver, Group(name="First", header="somt", footer="ghy"))
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_group(driver, Group(name="", header="", footer=""))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def create_group(self, driver, group):

        self.open_groups_page(driver)
        driver.find_element_by_name("new").click()
        # Fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)

        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page(driver)

    def open_groups_page(self, driver):
        # open groups page
        driver.find_element_by_link_text("groups").click()

    def login(self, driver, username, password):
        self.open_home_page(driver)
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()
