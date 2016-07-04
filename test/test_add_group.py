from model.group import Group


def test_add_group(app):
    app.session.login(username='admin', password='secret')
    app.group.create(Group(name='dfgdfg', header='dfgdfg', footer='dfgdfgdfg'))
    app.session.logout()


def test_empty_add_group(app):
    app.session.login(username='admin', password='secret')
    app.group.create(Group(name='', header='', footer=''))
    app.session.logout()
