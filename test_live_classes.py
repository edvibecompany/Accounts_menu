from selene import browser, have, be

def test_account_teacher():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('div.auth-form.auth-container > form > button:nth-child(4)').should(be.visible))
    browser.element('div.auth-form.auth-container > form > button:nth-child(4)').click()
    browser.wait_until(have.url('https://edvibe.com/TeacherAccount/lessons'))
    browser.element('.account-select-container').click()
    browser.element('.accounts-container').should(be.visible)
    browser.element('div.accounts-list > div:nth-child(6)').click()
    browser.should(have.url('https://preview.edvibe.com/student/lessons'))
    browser.element('.account-select').click()
    browser.element('div.accounts-list > div:nth-child(1)').click()
    browser.should(have.url_containing('/TeacherAccount/lessons'))
