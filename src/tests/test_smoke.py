from page_objects.feed_screen import PlayerScreen
from page_objects.preview_screen import PreviewScreen


def test_smoke(driver):
    PreviewScreen(driver).skip_preview()
    ps = PlayerScreen(driver)
    ps.all_elements_present()
    ps.user_can_swipe_the_video()
    ps.click_button_hide()
    ps.pause_is_working()
    ps.earning_when_watching_the_video()

