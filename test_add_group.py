import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username='admin', password='secret')
    app.create_group(Group(name='dfgdfg', header='dfgdfg', footer='dfgdfgdfg'))
    app.logout()


def test_empty_add_group(app):
    app.login(username='admin', password='secret')
    app.create_group(Group(name='', header='', footer=''))
    app.logout()
