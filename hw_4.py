def print_funk(funk, *args):
    funk_2 = funk.__name__.replace('_', ' ').capitalize()
    print(funk_2, ':', *args)


def open_browser(browser_name):
    print_funk(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_funk(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_funk(find_registration_button_on_login_page, page_url, button_text)


open_browser('Google Chrome')
go_to_companyname_homepage('https://qa.guru')
find_registration_button_on_login_page("https://qa.guru", "Записаться на первое занятие")

