import time

import allure
from selenium.common.exceptions import TimeoutException

from page_objects.base_screen import BaseScreen

from selenium.webdriver.common.by import By


class SpotsScreen(BaseScreen):
    TITLE_SPOTS = (By.ID, 'com.litit.app:id/tv_title')

    def _verify_screen(self) -> None:
        with allure.step('Checking that is really spots screen'):
            self.on_this_screen(self.TITLE_SPOTS)
