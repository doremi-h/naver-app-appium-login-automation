from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Android"
options.udid = "R3CY70KST6E"
options.no_reset = True

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 20)

try:
    naver_id = os.getenv("NAVER_ID")
    naver_pw = os.getenv("NAVER_PW")

    if not naver_id:
        raise ValueError("NAVER_ID 환경변수를 먼저 설정해야 합니다.")
    if not naver_pw:
        raise ValueError("NAVER_PW 환경변수를 먼저 설정해야 합니다.")

    print("1. 네이버 앱 실행")
    driver.activate_app("com.nhn.android.search")
    time.sleep(3)

    print("2. 메뉴 버튼 클릭")
    wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "com.nhn.android.search:id/slideMenuView")
        )
    ).click()

    print("3. 로그인 버튼 클릭")
    wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "com.nhn.android.search:id/nicknameView")
        )
    ).click()

    print("4. 아이디 입력")
    id_input = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.ID, "com.nhn.android.search:id/idText")
        )
    )
    id_input.click()
    id_input.clear()
    id_input.send_keys(naver_id)

    print("5. 비밀번호 입력")
    pw_input = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.ID, "com.nhn.android.search:id/passwordText")
        )
    )
    pw_input.click()
    pw_input.clear()
    pw_input.send_keys(naver_pw)

    print("6. 로그인 버튼 클릭")
    wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "com.nhn.android.search:id/button")
        )
    ).click()

    time.sleep(5)


    print("7. 메일 텍스트의 부모 클릭")
    mail_parent = wait.until(
        EC.element_to_be_clickable(
            (
                AppiumBy.XPATH,
                "//*[@text='메일']/ancestor::*[@clickable='true'][1]"
            )
        )
    )
    mail_parent.click()

    input("메일 화면 진입 여부 확인 후 엔터 누르세요...")

finally:
    driver.quit()