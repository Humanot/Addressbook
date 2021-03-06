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
    group_test = Contact(firstname="George", middlename="NA", lastname="Mironov", nickname="Human", photo="C:\\Users\\Human\\Desktop\\687227016.jpg",
                         title="QA", company="Blizzard", address="LA", homephone="122345", mobilephone="89302222", workphone="6666", fax="NA", email="Blizz@gmail.com",
                         email2="Blizz@gmail2.com", email3="Blizz@gmail2.com", homepage="mine.ru", bday="19", bmonth="December", byear="1990", aday="19",
                         amonth="December", ayear="2022", group=group_name, address2="New York", phone2="8747", notes="Hallow, guys!")
    app.contact.create(group_test)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(group_test)
    assert sorted(old_contacts, key=Contact.max_id) == sorted(new_contacts, key=Contact.max_id)

'''
def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                               homephone="", mobilephone="", workphone="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-",
                               byear="", aday="", amonth="-", ayear="", group="[none]", address2="", phone2="", notes=""))
'''