# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group

def test_add_contact(app):
    count = app.contact.get_group_options()

    if len(count) == 1:
        group = Group(name="wow")
        app.group.create(group)
        group_name = group.name
    else:
        group_name = count[1].name

    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="George", middlename="NA", lastname="Mironov", nickname="Human", photo="C:\\Users\\Human\\Desktop\\687227016.jpg",
                               title="QA", company="Blizzard", address="LA", home="122345", mobile="89302222", work="6666", fax="NA", email="Blizz@gmail.com",
                               email2="Blizz@gmail2.com", email3="Blizz@gmail2.com", homepage="mine.ru", bday="19", bmonth="December", byear="1990", aday="19",
                               amonth="December", ayear="2022", group=group_name, address2="New York", phone2="8747", notes="Hallow, guys!"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                               home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-",
                               byear="", aday="", amonth="-", ayear="", group="[none]", address2="", phone2="", notes=""))