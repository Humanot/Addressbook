from model.group import Group

def test_edit_group_name(app):
    app.group.edit_first(Group(name="Fucking brandnew name"))
