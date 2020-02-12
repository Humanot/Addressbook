from model.contact import Contact

def test_edit_mobile_field(app):
    if app.contact.count() == 0:
            app.contact.create(Contact(firstname="George", middlename="NA", lastname="Mironov", nickname="Human", photo="C:\\Users\\Human\\Desktop\\687227016.jpg",
                                       title="QA", company="Blizzard", address="LA", homephone="122345", mobilephone="89302222", workphone="6666", fax="NA", email="Blizz@gmail.com",
                                       email2="Blizz@gmail2.com", email3="Blizz@gmail2.com", homepage="mine.ru", bday="19", bmonth="December", byear="1990", aday="19",
                                       amonth="December", ayear="2022", group="[none]", address2="New York", phone2="8747", notes="Hallow, guys!"))
    app.contact.edit(Contact(mobilephone="890384726"))