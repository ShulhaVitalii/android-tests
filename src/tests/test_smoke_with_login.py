from page_objects.login_screen import LoginScreen
from page_objects.feed_screen import PlayerScreen
from page_objects.preview_screen import PreviewScreen


def test_smoke_with_login(driver):
    PreviewScreen(driver).skip_preview()
    PlayerScreen(driver).go_to_login_page()
    LoginScreen(driver).login()
    PlayerScreen(driver)
    ps = PlayerScreen(driver)
    ps.button_spots_is_on_the_feed_screen()
    ps.all_elements_present()
    ps.user_can_swipe_the_video()
    ps.click_button_hide()
    ps.pause_is_working()
    ps.earning_when_watching_the_video()

