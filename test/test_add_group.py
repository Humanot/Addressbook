# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="First", header="somt", footer="ghy"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))



