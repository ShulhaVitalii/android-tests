import allure
from selenium.common.exceptions import TimeoutException
from page_objects.base_screen import BaseScreen
from selenium.webdriver.common.by import By


class ExploreScreen(BaseScreen):
    LEADERBOARD_JUST_JOINED = (By.ID, 'com.litit.app:id/tab_joined')
    LEADERBOARD_REFERRALS = (By.ID, 'com.litit.app:id/tab_referrals')
    LEADERBOARD_POINTS = (By.ID, 'com.litit.app:id/tab_points')

    def _verify_screen(self) -> None:
        with allure.step('Checking that is really player screen'):
            self.on_this_screen(self.LEADERBOARD_POINTS)

