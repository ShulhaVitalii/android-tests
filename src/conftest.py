import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True, scope='function')
def driver():
    desired_capabilities = {
        'platformName': 'Android',
        'platformVersion': '8',
        'deviceName': 'Android Emulator',
        'app': 'c:\\app-prod.apk',
        #'noReset': True
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    driver.implicitly_wait(10)

    yield driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)


@pytest.fixture(scope='function', autouse=True)
def test_failed_check(request, driver):
    yield

    if request.node.rep_setup.failed:
        print('setting up a test failed!', request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            test_name = request.node.name
            print('executing test failed', request.node.nodeid)
            allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
            driver.save_screenshot('last_run.png')
