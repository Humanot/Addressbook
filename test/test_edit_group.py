from model.group import Group
from random import randrange

def test_edit_group_name(app):
    validate_group_exists(app)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="brandnew name")
    group.id = old_groups[index].id
    app.group.edit_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def validate_group_exists(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
