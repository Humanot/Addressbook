from model.group import Group

def test_edit_group_name(app):
    validate_group_exists(app)
    old_groups = app.group.get_group_list()
    group = Group(name="brandnew name")
    group.id = old_groups[0].id
    app.group.edit_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    print(old_groups[0])
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def validate_group_exists(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
