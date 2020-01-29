from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        # open groups page
        driver = self.app.driver
        if not (driver.current_url.endswith("/group.php") and len(driver.find_elements_by_name("new")) > 0):
            driver.find_element_by_link_text("groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first(self):
        driver = self.app.driver
        self.open_groups_page()
        # select first group
        self.select_first_group()
        # submit deletion
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_first(self, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        # select first group
        self.select_first_group()
        # submit deletion
        driver.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        driver.find_element_by_name("update").click()
        # submit group update
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, value):
        driver = self.app.driver
        if value is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(value)

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_groups_page()
            self.group_cache = []
            for element in driver.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

