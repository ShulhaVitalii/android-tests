import allure
from selenium.common.exceptions import TimeoutException
from page_objects.base_screen import BaseScreen
from selenium.webdriver.common.by import By


class CreateScreen(BaseScreen):
    BUTTON_UPLOAD = (By.ID, f'com.litit.app:id/tvUploadFromGallery')
    TEXT_BUTTON_UPLOAD = (By.ID, f'com.litit.app:id/tvUploadFromCamera')
    BUTTON_SHOOT_A_SPOT = (By.ID, f'com.litit.app:id/tvUploadSpots')
    TEXT_BUTTON_SHOOT_A_SPOT = (By.ID, f'com.litit.app:id/tvUploadSpotsDesc')
    BUTTON_RECORD = (By.ID, f'com.litit.app:id/tvUploadFromCamera')
    TEXT_BUTTON_RECORD = (By.ID, f'com.litit.app:id/tvUploadFromCameraDesc')

    def _verify_screen(self) -> None:
        with allure.step('Checking that is really player screen'):
            self.on_this_screen(self.BUTTON_UPLOAD)
