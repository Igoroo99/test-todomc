from tests_todomvc.model import app


def test_common_todo_functionality():
    app.visit()

    app.create('a', 'b', 'c')
    app.should_have('a', 'b', 'c')

    app.edit('b', 'b edited')

    app.toggle('b edited')

    app.clear_completed()
    app.should_have('a', 'c')

    app.cancel_editing('c', 'to be canceled')

    app.delete('c')
    app.should_have('a')
