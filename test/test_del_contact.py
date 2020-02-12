from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
            app.contact.create(Contact(firstname="George", middlename="NA", lastname="Mironov", nickname="Human", photo="C:\\Users\\Human\\Desktop\\687227016.jpg",
                                       title="QA", company="Blizzard", address="LA", homephone="122345", mobilephone="89302222", workphone="6666", fax="NA", email="Blizz@gmail.com",
                                       email2="Blizz@gmail2.com", email3="Blizz@gmail2.com", homepage="mine.ru", bday="19", bmonth="December", byear="1990", aday="19",
                                       amonth="December", ayear="2022", group="[none]", address2="New York", phone2="8747", notes="Hallow, guys!"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    a = app.contact.count()
    assert len(old_contacts) - 1 == a
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts