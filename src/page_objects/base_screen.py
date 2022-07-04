import abc
import time

import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


# Base class for all page objects


class BaseScreen(abc.ABC):
    BUTTON_ME = (By.ID, f'com.litit.app:id/userProfileFragmentFromBottom')
    BUTTON_SKIP = (By.ID, f'com.litit.app:id/btnSkip')
    BUTTON_START = (By.ID, f'com.litit.app:id/btStart')
    START_MASSAGE = (MobileBy.ID, f"com.litit.app:id/message")
    ANIM_VIEW = (By.ID, f'com.litit.app:id/anim_view')
    OK_BUTTON = (By.ID, f'com.litit.app:id/button_positive')
    # BUTTON_EXPLORE = (By.ID, f'com.litit.app:id/navigation_bar_item_icon_view')
    BUTTON_EXPLORE = (By.ID, f'com.litit.app:id/discoverFragment')
    BUTTON_ACTIVITY = (By.ID, f'com.litit.app:id/profileNotificationsFragment')
    BUTTON_CREATE = (By.ID, f'com.litit.app:id/create')

    def __init__(self, driver):
        self.driver = driver
        self._verify_screen()

    @abc.abstractmethod
    def _verify_screen(self) -> None:
        pass

    def get_element(self, locator, timeout=None) -> webelement:
        timeout = timeout or 20  # todo fixme
        with allure.step(f'Getting element with locator {locator} and timeout {timeout}'):
            expected_condition = ec.presence_of_element_located(locator)
            error_message = f'Unable to locate element {locator[1]} in {timeout} seconds'
            return WebDriverWait(self.driver, timeout).until(expected_condition, message=error_message)

    def get_element_1(self, locator):
        element = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator))
        return element

    def get_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def enter_text(self, locator, text, timeout=None) -> None:
        self.get_element(locator, timeout).send_keys(text)

    def get_text(self, locator, timeout=None):
        with allure.step(f'Getting text from locator {locator}'):
            return self.get_element(locator, timeout).text

    def on_this_screen(self, *args, timeout=30) -> None:
        with allure.step(f'Verifying that element with locator {args} present on screen'):
            timeout = timeout or self.driver.desired_capabilities['timeouts']['implicit']
            for locator in args:
                try:
                    self.get_element(locator, timeout)
                except TimeoutException:
                    raise Exception(f'Failed to find {locator[1]} in {timeout} seconds')

    def click_element(self, locator, timeout=None) -> None:
        with allure.step(f'Clicking element with locator {locator}'):
            self.get_element(locator, timeout).click()

    def wait_until_invisible(self, locator, timeout=None):
        error_message = 'Element {} is still visible after {} seconds'.format(locator, timeout)
        timeout = timeout or 10  # todo fixme
        WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator), message=error_message)

    def go_to_login_page(self):
        self.click_element(self.BUTTON_ME)
        time.sleep(1)

    def go_to_explore_screen(self):
        self.click_element(self.BUTTON_EXPLORE)

    def go_to_me_screen(self):
        self.click_element(self.BUTTON_ME)

    def go_to_activity_screen(self):
        self.click_element(self.BUTTON_ACTIVITY)

    def go_to_create_screen(self):
        self.click_element(self.BUTTON_CREATE)

    def swipe_up(self, t=100):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x1 = int(x * 0.5)
        y1 = int(y * 0.8)
        y2 = int(y * 0.2)
        self.driver.swipe(x1, y1, x1, y2, t)
        time.sleep(1)

    def should_be_start_massage(self):
        el = self.get_element_1(self.START_MASSAGE)
        assert el.text() == 'Swipe up to see more'

    def skip_preview(self):
        try:
            self.click_element(self.OK_BUTTON, 1)
        except:
            ...
        try:
            self.click_element(self.BUTTON_SKIP)
        except:
            ...
        self.click_element(self.BUTTON_START)
        try:
            self.click_element(self.ANIM_VIEW)
            time.sleep(1)
        except:
            ...
        self.swipe_up()
        time.sleep(1)
        self.swipe_up()





