
from appium.webdriver.webdriver import WebDriver
import time
import os


def swipe_down(driver: WebDriver):
    execute_adb_command(driver, f'input touchscreen swipe 530 1420 530 1120')
    time.sleep(1)


def execute_adb_command(driver: WebDriver, command: str):
    execute_adb_command_internal(f'adb shell {command}')


def execute_adb_command_internal(command: str):
    os.system(command)

def get_env():
    return


"""desired_caps = {
    "deviceName": 'Galaxy S7',
    "platformName": "Android",
    "platformVersion": '8',
    "app": "lt://APP10016551652797860613360",
    "isRealMobile": True,
    "build": "Smoke Android",
    "name": f"Smoke Galaxy S7",
    "network": True,
    "visual": True,
    "video": True
}


def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        username = "v.shulha@mediatech.ai"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        accesskey = "zr2XQwT3VrnApdJK5dCLV8mX63kesgUxD9UiQeTF8D4ZihwVsM"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps,
            command_executor="https://"+username+":"+accesskey+"@beta-hub.lambdatest.com/wd/hub")
        button_skip = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((MobileBy.ID, "com.litit.app.dev:id/btnSkip")))
        button_skip.click()
        button_start = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((MobileBy.ID, "com.litit.app.dev:id/btStart")))
        button_start.click()
        time.sleep(3)

        start_massage = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((MobileBy.ID, "com.litit.app.dev:id/message")))
        assert start_massage == 'Swipe up to see more'

        x = driver.get_window_size()['width']
        print(x)
        y = driver.get_window_size()['height']
        print(y)
        x1 = int(x * 0.5)
        y1 = int(y * 0.8)
        y2 = int(y * 0.2)
        driver.swipe(x1, y1, x1, y2, 300)
        print('swiped')
        button_me = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((MobileBy.ID, "com.litit.app.dev:id/userProfileFragmentFromBottom")))
        assert button_me

        driver.quit()
    except:
        driver.quit()

startingTest()
"""
