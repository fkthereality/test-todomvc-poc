from selene import have, config
from selene.support.shared import browser


todo_list = browser.all('#todo-list>li')


def open_app():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    window_uploaded = "return $._data($('#clear-completed')[0], 'events')" \
                      ".hasOwnProperty('click')"
    browser.should(have.js_returned(True, window_uploaded))


def add(*texts):
    for text in texts:
        browser.element('#new-todo').type(text).press_enter()



def assert_todos(*texts):
    todo_list.should(have.exact_texts(*texts))


def start_editing(text, added_text):
    todo_list.element_by(have.exact_text(text)). \
        double_click()
    return todo_list.element_by(have.css_class('editing')). \
        element('.edit').set_value(added_text)


def cancel_editing(text, added_text):
    start_editing(text, added_text).press_escape()


def edit(text, added_text):
    start_editing(text, added_text).press_enter()


def delete(text):
    todo_list.element_by(have.exact_text(text)).hover(). \
        element('.destroy').click()


def complete(text):
    todo_list.element_by(have.exact_text(text)). \
        element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()



