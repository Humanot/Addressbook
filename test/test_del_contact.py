from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
            app.contact.create(Contact(firstname="George", middlename="NA", lastname="Mironov", nickname="Human", photo="C:\\Users\\Human\\Desktop\\687227016.jpg",
                               title="QA", company="Blizzard", address="LA", home="122345", mobile="89302222", work="6666", fax="NA", email="Blizz@gmail.com",
                               email2="Blizz@gmail2.com", email3="Blizz@gmail2.com", homepage="mine.ru", bday="19", bmonth="December", byear="1990", aday="19",
                               amonth="December", ayear="2022", group="[none]", address2="New York", phone2="8747", notes="Hallow, guys!"))
    app.contact.delete_first()