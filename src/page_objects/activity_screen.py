import allure
from selenium.common.exceptions import TimeoutException
from page_objects.base_screen import BaseScreen
from selenium.webdriver.common.by import By


class ActivityScreen(BaseScreen):
    ACTIVITY_TITLE = (By.ID, f'com.litit.app:id/toolbarTitle')

    def _verify_screen(self) -> None:
        with allure.step('Checking that is really player screen'):
            self.on_this_screen(self.ACTIVITY_TITLE)

