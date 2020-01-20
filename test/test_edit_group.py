from model.group import Group

def test_edit_group_name(app):
    validate_group_exists(app)
    app.group.edit_first(Group(name="Fucking brandnew name"))


def validate_group_exists(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
