from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

link = "https://github.com"


def test_github():
    browser.config.window_width = 1320
    browser.config.window_height = 1080
    browser.open(link)

    browser.element(".header-search-button").click()
    browser.element('#query-builder-test').click().send_keys('eroshenkoam/allure-example')
    browser.element('#query-builder-test').submit()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#76')).should(be.visible)



