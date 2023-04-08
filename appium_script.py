from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "Android Emulator",
    "appActivity": "org.wikipedia.main.MainActivity",
    "appPackage": "org.wikipedia",
    "app": "C:/Users/thoma/PycharmProjects/python-appium-automation/mobile_app/wikipedia.apk"
}

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
driver.implicitly_wait(5)

driver.find_element(By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button').click()
driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="Search Wikipedia"]').click()
driver.find_element(By.ID, 'org.wikipedia:id/page_toolbar_button_search)').send_keys('Python(Programming')

actual_text = driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text
expected_text = "Python (programming language)"

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()
