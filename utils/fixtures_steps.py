import allure
from selene import browser, by, be


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
