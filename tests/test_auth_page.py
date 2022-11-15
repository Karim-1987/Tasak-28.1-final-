import pytest
from pages.auth_page import AuthPage
from pages.base import WebPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from config import *


def test_automatic_highlighting_color_phone(web_browser):
    """  Автоматический переход на таб ПОЧТА из таб ТЕЛЕФОН. """
    page = AuthPage(web_browser)
    page.username.send_keys(valid_email)
    page.password.click()
    assert "Почта" in page.activ_highlighting_color_btn.get_text()


def test_automatic_highlighting_color_login(web_browser):
    """ Автоматический переход на таб ПОЧТА из таб ЛОГИН. """
    page = AuthPage(web_browser)
    page.tab_login.click()
    page.username.send_keys(valid_email)
    page.password.click()
    assert "Почта" in page.activ_highlighting_color_btn.get_text()


def test_automatic_highlighting_color_ls(web_browser):
    """ Автоматический переход на таб ПОЧТА из таб Лицевой счет. """
    page = AuthPage(web_browser)
    page.tab_ls.click()
    page.username.send_keys(valid_email)
    page.password.click()
    assert "Почта" in page.activ_highlighting_color_btn.get_text()


def test_authorisation_valid_email(web_browser):
    """ Авторизация с валидными данными (email - пароль). """
    page = AuthPage(web_browser)
    page.username.send_keys(valid_email)
    page.password.send_keys(valil_password)
    page.btn_enter.click()
    assert page.btn_exit.is_visible()


def test_authorisation_valid_phone(web_browser):
    """ Авторизация с валидными данными (телефон - пароль). """
    page = AuthPage(web_browser)
    page.username.send_keys(valid_phone)
    page.password.send_keys(valil_password)
    page.btn_enter.click()
    assert page.btn_exit.is_visible()


def test_authorisation_invalid(web_browser):
    """ Авторизация с невалидным паролем (почта - пароль). """
    page = AuthPage(web_browser)
    page.tab_email.click()
    page.username.send_keys(valid_email)
    page.password.send_keys(invalil_password)
    page.btn_enter.click()
    assert page.username_error.is_visible()


def test_color_btn_forgot_password(web_browser):
    """ Подсветка ссылки 'забыли пароль' при введение неверного логина или пароля. """
    page = AuthPage(web_browser)
    page.tab_email.click()
    page.username.send_keys(valid_email)
    page.password.send_keys(invalil_password)
    page.btn_enter.click()
    assert page.activ_highlighting_color_forgot_password.is_visible()


def test_link_vk(web_browser):
    """ Проверка перехода на страницу соцсети при нажатии на иконку ( vk ). """
    page = AuthPage(web_browser)
    page.btn_link_vk.click()
    assert 'https://oauth.vk.com/authorize' in page.get_current_url()


def test_link_ok(web_browser):
    """ Проверка перехода на страницу соцсети при нажатии на иконку ( ok ). """
    page = AuthPage(web_browser)
    page.btn_link_ok.click()
    assert 'https://connect.ok.ru/' in page.get_current_url()


def test_link_mail(web_browser):
    """ Проверка перехода на страницу поисковой системы при нажатии на иконку ( mail ). """
    page = AuthPage(web_browser)
    page.btn_link_mail.click()
    assert 'https://connect.mail.ru/' in page.get_current_url()


def test_link_google(web_browser):
    """ Проверка перехода на страницу поисковой системы при нажатии на иконку ( google ). """
    page = AuthPage(web_browser)
    page.btn_link_google.click()
    assert 'https://accounts.google.com/' in page.get_current_url()


def test_link_yandex(web_browser):
    """ Проверка перехода на страницу поисковой системы при нажатии на иконку ( yandex ). """
    page = AuthPage(web_browser)
    page.btn_link_yandex.click()
    assert 'https://passport.yandex.ru/' in page.get_current_url()


def test_button_registration(web_browser):
    """ Проверка ссылки 'зарегистрироваться'.  """
    page = AuthPage(web_browser)
    page.btn_link_registration.click()
    assert page.btn_registration.is_presented()


def tests_chat_viber(web_browser):
    """ Проверка перехода на чат в месенджер при нажатии на иконку ( viber ).
        для теста неоходимо, чтобы мышка оставалась неподвижной,
        иначе selenium не сможет корректно навести курсор  """

    page = AuthPage(web_browser)
    page.btn_link_chat.move_mouse()
    page.btn_link_viber.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert 'https://chats.viber.com/' in page.get_current_url()


def tests_chat_telegram(web_browser):
    """ Проверка перехода на чат в месенджер при нажатии на иконку ( telegram ).
        для теста неоходимо, чтобы мышка оставалась неподвижной,
        иначе selenium не сможет корректно навести курсор  """

    page = AuthPage(web_browser)
    page.btn_link_chat.move_mouse()
    page.btn_link_telega.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert 'https://telegram.me/' in page.get_current_url()


def tests_link_cookies(web_browser):
    """ Проверка инфо ссылки Cookies. """
    page = AuthPage(web_browser)
    page.btn_link_cookies.click()
    assert page.table_cookies.is_visible()


def tests_link_user_confidentiality(web_browser):
    """ Проверка инфо ссылки 'Политика конфиденциальности'. """
    page = AuthPage(web_browser)
    page.btn_link_confidentiality.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert 'https://b2c.passport.rt.ru/sso-static/agreement' in page.get_current_url()


def tests_link_user_agreement(web_browser):
    """ Проверка инфо ссылки 'Пользовательским соглашением'. """
    page = AuthPage(web_browser)
    page.btn_link_agreement.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert 'https://b2c.passport.rt.ru/sso-static/agreement' in page.get_current_url()


def tests_tab_email_256_cars_(web_browser):
    """ Проверка ограничения количества ввода символов ( 256 символов ). """
    page = AuthPage(web_browser)
    page.tab_email.click()
    page.username.send_keys(chars_256)
    page.password.send_keys(chars_256)
    page.btn_enter.click()
    assert page.username_error.is_visible()


def tests_tab_ls_1001_chars(web_browser):
    """ Проверка ограничения количества ввода символов ( 1001 символов ). """
    page = AuthPage(web_browser)
    page.tab_ls.click()
    page.username.send_keys(chars_1001)
    page.password.send_keys(chars_1001)
    page.btn_enter.click()
    assert page.username_error.is_visible()


def tests_invalid_phone(web_browser):
    """ Автоматический переход на таб ЛОГИН из таб ТЕЛЕФОН при вводе кирилицы. """
    page = AuthPage(web_browser)
    page.username.send_keys(invalid_phone)
    page.password.click()
    assert "Логин" in page.activ_highlighting_color_btn.get_text()
