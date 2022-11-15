from pages.base import WebPage
# from pages.elements import WebElement, ManyWebElements
from pages.elements import WebElement, ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    username = WebElement(id='username')
    password = WebElement(id='password')
    btn_enter = WebElement(id='kc-login')
    btn_exit = WebElement(id='logout-btn')
    tab_phone = WebElement(id='t-btn-tab-phone')
    tab_email = WebElement(id='t-btn-tab-mail')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')
    username_error = WebElement(xpath='//*[@id="page-right"]/div/div/p')
    activ_highlighting_color_btn = WebElement\
        (xpath='//div[@class="rt-tab rt-tab--small rt-tab--active"]')
    activ_highlighting_color_forgot_password = WebElement\
        (xpath='//a[@class="rt-link rt-link--orange '
               'login-form__forgot-pwd login-form__forgot-pwd--animated"]')
    btn_link_vk = WebElement(id='oidc_vk')
    btn_link_ok = WebElement(id='oidc_ok')
    btn_link_mail = WebElement(id='oidc_mail')
    btn_link_google = WebElement(id='oidc_google')
    btn_link_yandex = WebElement(id='oidc_ya')
    btn_link_registration = WebElement(id='kc-register')
    btn_registration = WebElement\
        (xpath='//button[@class="rt-btn rt-btn--orange '
               'rt-btn--medium rt-btn--rounded register-form__reg-btn"]')
    btn_link_chat = WebElement(xpath='//div[@class="icon  svelte-16eyo30"]')
    btn_link_viber = WebElement(xpath='//a[@class="alt-channel omnichat-theme-white svelte-16eyo30"][1]')
    btn_link_telega = WebElement(xpath='//a[@class="alt-channel omnichat-theme-white svelte-16eyo30"][2]')
    btn_link_cookies = WebElement(xpath='//span[contains(text(),"Cookies")]')
    table_cookies = WebElement\
        (xpath='//div[@class="rt-tooltip rt-tooltip--rounded rt-tooltip--topLeft rt-cookies-tip"]')
    btn_link_confidentiality = WebElement(xpath='//span[contains(text(),"Политикой конфиденциальности")]')
    btn_link_agreement = WebElement(xpath='//span[contains(text(),"Пользовательским соглашением")]')
