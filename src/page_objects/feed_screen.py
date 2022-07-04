import time

import allure
from selenium.common.exceptions import TimeoutException

from page_objects.base_screen import BaseScreen
from page_objects.spots_screen import SpotsScreen

from selenium.webdriver.common.by import By


class PlayerScreen(BaseScreen):    
    TEXT_AUTHOR_NAME = (By.ID, f'com.litit.app:id/author_name')
    SECTION_HASHTAG = (By.ID, f'com.litit.app:id/tv_description')
    PLAYER_CONTROL_PLAY = (By.ID, f'com.litit.app:id/player_control_play')
    BUTTON_COMMENTS = (By.ID, f'com.litit.app:id/button_comments')
    ANIMATION_MUSIC = (By.ID, f'com.litit.app:id/anim_music')
    BUTTON_HIDE = (By.ID, f'com.litit.app:id/button_hide')
    BUTTON_SHARE = (By.ID, f'com.litit.app:id/button_share')
    LIKE_COUNTER = (By.ID, f'com.litit.app:id/likes')
    LIKE_BUTTON = (By.ID, f'com.litit.app:id/vCircle')
    IMAGE_LIKE = (By.ID, f'com.litit.app:id/ivImage')
    BUTTON_SUGGESTIONS = (By.ID, f'com.litit.app:id/button_suggestions')
    BUTTON_UNLIKE = (By.ID, f'com.litit.app:id/button_unlike')
    BUTTON_TIP = (By.ID, f'com.litit.app:id/button_tip')
    SECTION_VIEWS = (By.ID, f'com.litit.app:id/views')
    ANIM_COIN = (By.ID, f'com.litit.app:id/anim_token_coin')
    TEXT_TOKENS_REALTIME = (By.ID, f'com.litit.app:id/text_tokens_realtime')
    BUTTON_SPOTS = (By.ID, f'com.litit.app:id/button_spots')
    BUTTON_TIP_CONFIRM = (By.ID, f'com.litit.app:id/btn_tip')
    TITLE_COMMENTS = (By.ID, f'com.litit.app:id/title')
    TITLE_SHARE = (By.ID, f'com.litit.app:id/tv_title')
    BUTTON_HELP = (By.ID, f'com.litit.app:id/button_feedback')
    TITLE_CUSTOMERS_SUPPORT = (By.ID, f'com.litit.app:id/tvTitle')

    TEXT_IN_UNLIKE_SCREEN = (By.ID, f'com.litit.app:id/tvThisVideo')

    elements = [TEXT_AUTHOR_NAME, ANIMATION_MUSIC, BUTTON_HIDE, BUTTON_SHARE, LIKE_BUTTON,
                LIKE_COUNTER, BUTTON_SUGGESTIONS, BUTTON_UNLIKE, BUTTON_TIP, SECTION_VIEWS]

    def _verify_screen(self) -> None:
        with allure.step('Checking that is really player screen'):
            self.on_this_screen(self.ANIM_COIN)

    def all_elements_present(self):
        for e in self.elements:
            self.get_element(e)

    def pause_is_working(self):
        try:
            self.click_element(self.ANIMATION_MUSIC)
        except:
            ...
        time.sleep(1)
        self.on_this_screen(self.PLAYER_CONTROL_PLAY)

    def user_can_swipe_the_video(self):
        author_name_before_swipe = self.get_text(self.TEXT_AUTHOR_NAME)
        hashtags_before = self.get_text(self.SECTION_HASHTAG)
        self.swipe_up()
        time.sleep(1)
        self.swipe_up()
        author_name_after_swipe = self.get_text(self.TEXT_AUTHOR_NAME)
        hashtags_after = self.get_text(self.SECTION_HASHTAG)
        time.sleep(1)
        with allure.step('Checking that author name or hashtags are not equal after swipe'):
            assert author_name_before_swipe != author_name_after_swipe or hashtags_after != hashtags_before

    def click_button_hide(self):
        self.click_element(self.ANIMATION_MUSIC)
        time.sleep(1)
        self.click_element(self.BUTTON_HIDE)
        time.sleep(1)
        flag = False
        try:
            self.get_element(self.TEXT_AUTHOR_NAME)
        except TimeoutException:
            flag = True
        with allure.step('Checking that buttons are hide'):
            assert flag is True

    def earning_when_watching_the_video(self):
        coin_amount_before = self.get_text(self.TEXT_TOKENS_REALTIME)
        print(coin_amount_before)
        self.swipe_up()
        time.sleep(1)
        self.swipe_up()
        time.sleep(1)
        self.swipe_up()
        time.sleep(10)
        coin_amount_after = self.get_text(self.TEXT_TOKENS_REALTIME)
        print(coin_amount_after)
        assert int(coin_amount_before) < int(coin_amount_after)

    def button_spots_is_on_the_feed_screen(self):
        self.on_this_screen(self.BUTTON_SPOTS)

    def click_on_tip_button(self):
        try:
            self.click_element(self.BUTTON_TIP)
            self.click_element(self.BUTTON_TIP)
        except:
            ...
        with allure.step('Checking that tip window is opened'):
            self.on_this_screen(self.BUTTON_TIP_CONFIRM)

    def click_on_spots_button(self):
        try:
            self.click_element(self.BUTTON_SPOTS)
            self.click_element(self.BUTTON_SPOTS)
        except:
            ...
        with allure.step('Checking that tip window is opened'):
            self.on_this_screen(SpotsScreen.TITLE_SPOTS)

    def click_on_comments_button(self):
        try:
            self.click_element(self.BUTTON_COMMENTS)
            self.click_element(self.BUTTON_COMMENTS)
        except:
            ...
        with allure.step('Checking that tip window is opened'):
            self.on_this_screen(self.TITLE_COMMENTS)

    def click_on_like_button(self):
        self.click_element(self.LIKE_BUTTON)
        is_enable = self.get_element(self.IMAGE_LIKE).get_attribute('enabled')
        print(is_enable)

        if is_enable is True:
            with allure.step('Checking that like image is enabled'):
                assert is_enable == 'true'
                print('cool')
        else:
            self.click_element(self.LIKE_BUTTON)
            is_enable = self.get_element(self.IMAGE_LIKE).get_attribute('enabled')
            print(is_enable)
            time.sleep(1)
            with allure.step('Checking that like image is enabled'):
                assert is_enable == 'true'

    def click_on_share_button(self):
        try:
            self.click_element(self.BUTTON_SHARE)
            self.click_element(self.BUTTON_SHARE)
        except:
            ...
        with allure.step('Checking that is share windows'):
            self.on_this_screen(self.TITLE_SHARE)

    def click_on_unlike_button(self):
        try:
            self.click_element(self.BUTTON_UNLIKE)
            self.click_element(self.BUTTON_UNLIKE)
        except:
            ...
        with allure.step('Checking that is window windows'):
            self.on_this_screen(self.TEXT_IN_UNLIKE_SCREEN)

    def click_on_help_button(self):
        try:
            self.click_element(self.BUTTON_HELP)
            self.click_element(self.BUTTON_HELP)
        except:
            ...
        with allure.step('Checking that is help window'):
            self.on_this_screen(self.TITLE_CUSTOMERS_SUPPORT)
