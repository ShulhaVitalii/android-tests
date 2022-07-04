from page_objects.activity_screen import ActivityScreen
from page_objects.create_screen import CreateScreen
from page_objects.explore_screen import ExploreScreen
from page_objects.login_screen import LoginScreen
from page_objects.feed_screen import PlayerScreen
from page_objects.preview_screen import PreviewScreen
from page_objects.base_screen import BaseScreen
from page_objects.spots_screen import SpotsScreen


def test_player_screen_displayed(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).swipe_up()


def test_all_elements_are_present(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).all_elements_present()


def test_video_pause_is_working(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).pause_is_working()


def test_user_can_swipe(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).user_can_swipe_the_video()


def test_elements_are_hide_after_click_button_hide(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).click_button_hide()


def test_earning_when_watching_the_video(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).earning_when_watching_the_video()


def test_login_with_email(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver)


def test_open_spots_feed(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver).click_on_spots_button()
    SpotsScreen(driver)


def test_tip_window_is_opened_after_click_on_tip_button(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver).click_on_tip_button()


def test_comments_window_is_opened_after_click_on_tip_button(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver).click_on_comments_button()


def test_like_button_is_changed_color_after_click(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver).click_on_like_button()


def test_click_on_share_button(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver).click_on_share_button()


def test_click_on_unlike_button(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver).click_on_unlike_button()


def test_click_on_help_button(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver).click_on_help_button()


def test_go_to_explore_screen(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver).go_to_explore_screen()
    ExploreScreen(driver)


def test_go_to_activity_screen(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver).go_to_activity_screen()
    ActivityScreen(driver)


def test_go_to_create_screen(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver).go_to_create_screen()
    CreateScreen(driver)
