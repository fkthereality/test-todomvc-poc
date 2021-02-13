from selene.api import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

config.hold_browser_open = True
config.hold_browser_open = False
config.type_by_js = True
config.timeout = 16
config.set_value_by_js = True


def press_enter_and_wait():
    time.sleep(3)
    ActionChains(browser.driver()) \
        .key_down(Keys.ENTER) \
        .key_up(Keys.ENTER) \
        .perform()
    time.sleep(3)
    browser.element('#new-todo').should(be.blank)
    return


def test_add_toggle_todos():
    browser.open_url('http://todomvc4tasj.herokuapp.com/')
    browser.element('#new-todo').type('a')
    press_enter_and_wait()
    browser.all('#todo-list>li')[0].should(have.exact_text('a'))
    browser.all('#todo-list>li').should(have.size(1))

    browser.element('#new-todo').type('b')
    press_enter_and_wait()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b'))

    browser.all('#todo-list>li').element_by(have.exact_text('a')).double_click()
    browser.all('.editing .edit').element_by(be.visible).type(' edited')
    press_enter_and_wait()
    browser.all('#todo-list>li').element_by(have.exact_text('a edited')). \
        element('.destroy').click()

    browser.all('#todo-list>li').element_by(have.exact_text('b'))\
        .double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing'))\
        .element('.edit').type(' edited')
    press_enter_and_wait()
    browser.all('#todo-list>li').element_by(have.exact_text('b edited'))\
        .element('.toggle').click()

    browser.all('#todo-list>li').filtered_by(have.css_class('completed'))\
        .should(have.exact_texts('b edited'))
    browser.all('#todo-list>li').filtered_by(have.css_class('active'))\
        .should(have.size(0))
    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.size(0))
