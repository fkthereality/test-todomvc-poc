from selene.support.shared import config
from test_todomvc_poc.helpers import app

config.set_value_by_js = True


def test_mvc_poc():
    app.open_app()

    app.add('a', 'b', 'c')

    app.assert_todos('a', 'b', 'c')

    app.cancel_editing('a', 'a to be canceled')

    app.delete('a')
    app.assert_todos('b', 'c')

    app.edit('b', 'b edited')

    app.complete('b edited')
    app.clear_completed()
    app.assert_todos('c')
