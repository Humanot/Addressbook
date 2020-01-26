from model.group import Group

def test_edit_group_name(app):
    validate_group_exists(app)
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(name="Fucking brandnew name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def validate_group_exists(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
