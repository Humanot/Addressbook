from model.contact import Contact

def test_edit_mobile_field(app):
    app.contact.edit(Contact(mobile="890384726"))