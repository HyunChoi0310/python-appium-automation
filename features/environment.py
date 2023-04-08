from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def driver_init(context, test_name):
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "Android Emulator",
        "appActivity": "org.wikipedia.main.MainActivity",
        "appPackage": "org.wikipedia",
        "app": "C:/Users/thoma/PycharmProjects/python-appium-automation/mobile_app/wikipedia.apk"
    }
    context.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                      desired_capabilities=desired_capabilities)

# #BrowserStack
# def driver_init(context, test_name):
#     desired_capabilities = {
#         "platformName": "Android",
#         "app": "bs://729af6a9cac9bf075a04f6aded3579a7931067ed",
#         "deviceName": "Google Pixel 3",
#         "os_version": "10.0",
#         'bstack:options': {
#             "userName": 'hyunredcloud_TPBt2u',
#             'sessionName': "BStack first time test",
#             'accessKey': '7jxNseRwHAsznZxPXda4'
#         }
#     }
#     remote_url = 'http://hub-cloud.browsersrack.com/wd/hub'
#
#     context.driver = webdriver.Remote(command_executor=remote_url,
#                                       desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(5)

    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    driver_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
