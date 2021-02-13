from selene import have, be
from selene.support.shared import browser


def test_mvc_poc():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    window_uploaded = "return $._data($('#clear-completed')[0], 'events')" \
                      ".hasOwnProperty('click')"
    browser.should(have.js_returned(True, window_uploaded))

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()

    browser.all('#todo-list>li').should(have.exact_texts('a', 'b'))

    browser.all('#todo-list>li').element_by(have.exact_text('a')). \
        double_click()
    browser.all('.editing .edit').element_by(be.visible). \
        type(' to be canceled').press_escape()

    browser.all('#todo-list>li').element_by(have.exact_text('a')).hover(). \
        element('.destroy').click()

    browser.all('#todo-list>li').element_by(have.exact_text('b')). \
        double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing')). \
        element('.edit').type(' edited').press_enter()

    browser.all('#todo-list>li').element_by(have.exact_text('b edited')). \
        element('.toggle').click()

    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.size(0))
