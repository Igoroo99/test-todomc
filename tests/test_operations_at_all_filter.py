from selenium.webdriver.common.keys import Keys
from tests_todomvc.model import app


def test_create_first_one():
    app.given_opened_with()

    # WHEN nothing
    app.create()

    app.should_have_no_todos()
    app.should_nave_hidden_footer()

    # WHEN
    app.create('a')

    app.should_have('a')
    app.should_have_items_left(1)


def test_create_many():
    app.given_opened_with()

    app.create('a', 'b')

    app.should_have('a', 'b')
    app.should_have_items_left(2)


def test_edit():
    app.given_opened_with('a', 'b', 'c')

    app.edit('b', 'b edited')

    app.should_have('a', 'b edited', 'c')
    app.should_have_items_left(3)


def test_edit_by_focus_change():
    app.given_opened_with('a', 'b', 'c')

    app.edit('b', 'b edited', Keys.TAB)

    app.should_have('a', 'b edited', 'c')
    app.should_have_items_left(3)


def test_cancel_editing():
    app.given_opened_with('a', 'b', 'c')

    app.cancel_editing('b', 'to be canceled')

    app.should_have('a', 'b', 'c')
    app.should_have_items_left(3)


def test_delete_by_edit_blank():
    app.given_opened_with('a', 'b', 'c')

    app.edit('b', '')

    app.should_have('a', 'c')
    app.should_have_items_left(2)


def test_complete():
    app.given_opened_with('a', 'b', 'c')

    app.toggle('b')

    app.should_have_completed('b')
    app.should_have_active('a', 'c')
    app.should_have_items_left(2)
    app.should_have_clear_completed_visible()


def test_activate():
    app.given_opened_with('a', 'b', 'c')
    app.toggle('b')

    app.toggle('b')

    app.should_have_completed()
    app.should_have_active('a', 'b', 'c')
    app.should_have_items_left(3)
    app.should_have_clear_completed_hidden()


def test_complete_all():
    app.given_opened_with('a', 'b', 'c')
    app.toggle('b')

    app.toggle_all()

    app.should_have_active()
    app.should_have_completed('a', 'b', 'c')
    app.should_have_items_left(0)
    app.should_have_clear_completed_visible()


def test_activate_all():
    app.given_opened_with('a', 'b', 'c')
    app.toggle_all()

    app.toggle_all()

    app.should_have_active('a', 'b', 'c')
    app.should_have_completed()
    app.should_have_items_left(3)
    app.should_have_clear_completed_hidden()


def test_clear_completed():
    app.given_opened_with('a', 'b', 'c', 'd')
    app.toggle('b')
    app.toggle('d')

    app.clear_completed()

    app.should_have('a', 'c')
    app.should_have_items_left(2)
    app.should_have_clear_completed_hidden()


def test_delete():
    app.given_opened_with('a', 'b', 'c')

    app.delete('b')

    app.should_have('a', 'c')
    app.should_have_items_left(2)


def test_delete_last_todo():
    app.given_opened_with('a')

    app.delete('a')

    app.should_have_no_todos()
    app.should_nave_hidden_footer()





