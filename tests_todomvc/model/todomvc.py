from selene import have, be
from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys


be_completed = have.css_class('completed')
be_active = be_completed.not_


class TodoMvc:
    def visit(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        app_loaded_js = "return $._data($('#clear-completed')[0],'events')"\
                        ".hasOwnProperty('click')"
        browser.should(have.js_returned(True, app_loaded_js))
        return self

    def given_opened_with(self, *todos: str):
        self.visit()
        self.create(*todos)
        return self

    def __init__(self):
        self._list = browser.all('#todo-list>li')
        self._clear_completed_button = browser.element('#clear-completed')

    def create(self, *todos: str):
        for todo in todos:
            browser.element('#new-todo').set_value(todo).press_enter()
        return self

    def should_have(self, *todos: str):
        self._list.should(have.exact_texts(*todos))
        return self

    def should_have_no_todos(self):
        return self.should_have()

    def start_editing(self, todo, new_text: str):
        self._list.element_by(have.exact_text(todo)).double_click()
        return self._list.element_by(have.css_class('editing'))\
            .element('.edit').with_(set_value_by_js=True).set_value(new_text)

    def edit(self, todo: str, new_text, submit_by=Keys.ENTER):
        self.start_editing(todo, new_text).press(submit_by)
        return self

    def cancel_editing(self, todo: str, new_text):
        self.start_editing(todo, new_text).press(Keys.ESCAPE)
        return self

    def toggle(self, todo):
        self._list.element_by(have.exact_text(todo)).element('.toggle').click()

    def should_have_completed(self, *todos: str):
        self._list.filtered_by(have.css_class('completed')).should(have.exact_texts(*todos))
        return self

    def should_have_active(self, *todos: str):
        self._list.filtered_by(have.css_class('active')).should(have.exact_texts(*todos))
        return self

    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    def delete(self, todo: str):
        self._list.element_by(have.exact_text(todo)).hover() \
            .element('.destroy').click()
        return self

    def should_have_items_left(self, amount):
        browser.element('#todo-count>strong') \
            .should(have.exact_text(str(amount)))
        return self

    def should_nave_hidden_footer(self):
        browser.element('#footer').should(be.not_.visible)
        return self

    def should_have_clear_completed_visible(self):
        self._clear_completed_button.should(be.visible)
        return self

    def should_have_clear_completed_hidden(self):
        self._clear_completed_button.should(be.not_.visible)
        return self
