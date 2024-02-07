import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


@allure.step('Настраиваем браузер')
def config_browser():
    browser.config.window_width = 1320
    browser.config.window_height = 1080


@allure.step('Открываем страницу по ссылке')
def go_to_the_link():
    browser.open("https://github.com")


@allure.step('Ищем репозиторий {repo}')
def find_repository(repo):
    browser.element(".header-search-button").click()
    browser.element('#query-builder-test').click().send_keys(repo)
    browser.element('#query-builder-test').submit()


@allure.step('Переходим по ссылке {repo}')
def going_to_the_link(repo):
    browser.element(by.link_text(repo)).click()
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие Issue {number}')
def checking_issue(number):
    browser.element(by.partial_text(number)).should(be.visible)
