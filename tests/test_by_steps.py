import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from utils.fixtures_steps import config_browser, going_to_the_link, find_repository, go_to_the_link, checking_issue


@allure.tag('Github')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Rustam')
@allure.feature("Tasks in repository")
@allure.story('Checking issue № 76')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    config_browser()
    go_to_the_link()
    find_repository('eroshenkoam/allure-example')
    going_to_the_link('eroshenkoam/allure-example')
    checking_issue('#76')


@allure.tag('Github')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'Rustam')
@allure.feature("Tasks in repository")
@allure.story('Checking issue № 76')
@allure.link('https://github.com', name='Testing')
def test_github():
    with allure.step('Настраиваем браузер'):
        browser.config.window_width = 1320
        browser.config.window_height = 1080

    with allure.step('Открываем страницу по ссылке'):
        browser.open("https://github.com")

    with allure.step('Ищем репозиторий'):
        browser.element(".header-search-button").click()
        browser.element('#query-builder-test').click().send_keys('eroshenkoam/allure-example')
        browser.element('#query-builder-test').submit()

    with allure.step('Переходим по ссылке'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие Issue №76'):
        browser.element(by.partial_text('#76')).should(be.visible)
