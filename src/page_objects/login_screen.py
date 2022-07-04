import time

import allure
from selenium.webdriver.common.by import By

from page_objects.base_screen import BaseScreen
from page_objects.feed_screen import PlayerScreen


class LoginScreen(BaseScreen):
    """
    Test users for prod
    dismasdarkin1655363137@gmail.com
    dismasdarkin1655363166@gmail.com
    dismasdarkin1655363174@gmail.com
    dismasdarkin1655363182@gmail.com
    dismasdarkin1655363191@gmail.com
    q12345q.
    """
    TITLE = (By.ID, 'com.litit.app:id/tvTitle')
    SIGN_UP_WITH_EMAIL = (By.ID, 'com.litit.app:id/btnEmail')
    BUTTON_GO_TO_LOGIN = (By.ID, 'com.litit.app:id/tvBottom')

    INPUT_EMAIL = (By.ID, 'com.litit.app:id/edtEmail')
    INPUT_PASSWORD = (By.ID, 'com.litit.app:id/edtPassword')

    INPUT_NICKNAME = (By.ID, 'com.litit.app:id/textinput_placeholder')

    INPUT_PASSWORD_REGISTRATION = (By.ID, 'com.litit.app:id/edtPass')
    INPUT_PASSWORD_REGISTRATION2 = (By.ID, 'com.litit.app:id/edtPass2')
    INPUT_FIRSTNAME = (By.ID, 'com.litit.app:id/edtFirstName')
    INPUT_LASTNAME = (By.ID, 'com.litit.app:id/edtSecondName')
    BUTTON_CONTINUE = (By.ID, 'com.litit.app:id/btnContinue')

    LOGIN_WITH_EMAIL = (By.ID, 'com.litit.app:id/btnEmail')

    GENDER = (By.ID, 'com.litit.app:id/root')

    user_1_email = "dismasdarkin1655363137@gmail.com"
    user_1_password = "q12345q."
    nickname = 'AutoUI'
    firstname = 'Auto'
    lastname = 'UI'

    def _verify_screen(self) -> None:
        with allure.step('Checking that is really login screen'):
            self.on_this_screen(self.TITLE)

    def registration(self):
        self.click_element(self.SIGN_UP_WITH_EMAIL)
        input_login = self.get_element(self.INPUT_EMAIL)
        input_login.clear().send_keys(self.user_1_email)
        self.click_element(self.BUTTON_CONTINUE)

        input_password = self.get_element(self.INPUT_PASSWORD_REGISTRATION)
        input_password.clear().send_keys(self.user_1_password)

        confirm_password = self.get_element(self.INPUT_PASSWORD_REGISTRATION2)
        confirm_password.clear().send_keys(self.user_1_password)
        self.click_element(self.BUTTON_CONTINUE)

        input_nickname = self.get_element(self.INPUT_NICKNAME)
        input_nickname.clear().send_keys(self.nickname)
        self.click_element(self.BUTTON_CONTINUE)

        self.click_element(self.GENDER)
        self.click_element(self.BUTTON_CONTINUE)

        input_firstname = self.get_element(self.INPUT_FIRSTNAME)
        input_firstname.clear().send_keys(self.firstname)

        input_lastname = self.get_element(self.INPUT_LASTNAME)
        input_lastname.clear().send_keys(self.lastname)

        self.click_element(self.BUTTON_CONTINUE)
        time.sleep(1)
        self.click_element(self.BUTTON_CONTINUE)
        time.sleep(1)
        self.click_element(self.BUTTON_CONTINUE)
        self.click_element(self.BUTTON_SKIP)

    def login(self):
        self.click_element(self.BUTTON_GO_TO_LOGIN)
        self.click_element(self.LOGIN_WITH_EMAIL)
        input_login = self.get_element(self.INPUT_EMAIL)
        input_login.clear().send_keys(self.user_1_email)

        input_password = self.get_element(self.INPUT_PASSWORD)
        input_password.clear().send_keys(self.user_1_password)

        self.click_element(self.BUTTON_CONTINUE)
        time.sleep(1)
