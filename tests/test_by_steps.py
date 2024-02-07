import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

link = "https://github.com"


def test_github():
    with allure.step('Настраиваем браузер'):
        browser.config.window_width = 1320
        browser.config.window_height = 1080

    with allure.step('Открываем страницу по ссылке'):
        browser.open(link)

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



