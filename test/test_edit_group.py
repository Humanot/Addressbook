from model.group import Group

def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="Fucking brandnew name"))
    app.session.logout()