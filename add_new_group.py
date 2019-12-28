# -*- coding: utf-8 -*-
from group import Group
from application import Application
import unittest

class add_new_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_add_new_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="First", header="somt", footer="ghy"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()
