from selenium.webdriver.support.ui import Select
from model.group import Group
from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        self.open_new_contact_page()
        self.fill_contact_form(contact)

        #submit_creation of contact
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def open_new_contact_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.add_file("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # Birthday date
        self.change_listbox_item("bday", contact.bday)
        self.change_listbox_item("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        # Anniversary date
        self.change_listbox_item("aday", contact.aday)
        self.change_listbox_item("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_listbox_item("new_group", contact.group)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def edit(self, contact):
        driver = self.app.driver
        self.select_first_edit_tool()
        self.change_field_value("mobilephone", contact.mobile)
        driver.find_element_by_xpath("//form[@enctype='multipart/form-data']//*[@name='update']").click()
        self.contact_cache = None

    def select_edit_tool_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_xpath("//*[@Title='Edit']")[index].click()

    def select_first_edit_tool(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//*[@Title='Edit']").click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        driver = self.app.driver
        self.select_edit_tool_by_index(index)
        driver.find_element_by_xpath("//*[@name='update' and @value='Delete']").click()
        driver.find_element_by_css_selector('#container #content .msgbox').text == "Record successful deleted"
        self.contact_cache = None


    def change_listbox_item(self, listbox_name, item):
        driver = self.app.driver
        driver.find_element_by_name(listbox_name).click()
        Select(driver.find_element_by_name(listbox_name)).select_by_visible_text(item)
        driver.find_element_by_name(listbox_name).click()

    def add_file(self, element_name, value):
        driver = self.app.driver
        if value is not None:
            driver.find_element_by_name(element_name).send_keys(value)

    def change_field_value(self, field_name, value):
        driver = self.app.driver
        if value is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(value)

    def count(self):
        driver = self.app.driver
        self.app.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

    def get_group_options(self):
        driver = self.app.driver
        self.open_new_contact_page()
        group_items = []
        for item in driver.find_elements_by_css_selector(("select[name=new_group] option")):
            text = item.text
            group_items.append(Group(name=text))

        return group_items

    def open_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def view_details_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.app.open_home_page()
            self.contact_cache = []
            for row in driver.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute('id')
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_home_page_phones=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        phone2 = driver.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.view_details_by_index(index)
        text = driver.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2)