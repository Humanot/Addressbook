from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)

        #submit_creation of contact
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("home page").click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.add_file("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
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
        self.select_edit_tool()
        self.change_field_value("mobile", contact.mobile)
        driver.find_element_by_xpath("//form[@enctype='multipart/form-data']//*[@name='update']").click()

    def select_edit_tool(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//*[@Title='Edit']").click()

    def delete_first(self):
        driver = self.app.driver
        self.select_edit_tool()
        driver.find_element_by_xpath("//*[@name='update' and @value='Delete']").click()
        driver.find_element_by_css_selector('#container #content .msgbox').text == "Record successful deleted"


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