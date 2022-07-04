import time

from selenium.common.exceptions import TimeoutException

from page_objects.base_screen import BaseScreen

from selenium.webdriver.common.by import By


class PreviewScreen(BaseScreen):

    def _verify_screen(self) -> None:
        pass
