from model.group import Group


def test_add_group(app):
    app.group.create(Group(name='dfgdfg', header='dfgdfg', footer='dfgdfgdfg'))


def test_empty_add_group(app):
    app.group.create(Group(name='', header='', footer=''))
