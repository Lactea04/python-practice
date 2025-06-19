
#이 소스코드는 chat gpt한테 소스코드 작성을 부탁한 뒤 일부 수정한 것임


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 사용자 입력 받기
user_id = input("아이디를 입력하세요: ")
user_pw = input("비밀번호를 입력하세요: ")

# 웹드라이버 실행 (Chrome 기준)
driver = webdriver.Chrome()

try:
    # 포털 사이트 접속
    driver.get("https://sso.gachon.ac.kr/svc/tk/Auth.do?ac=Y&ifa=N&id=portal&")
    time.sleep(2)  # 페이지 로딩 대기

    # 아이디 입력
    id_input = driver.find_element(By.CSS_SELECTOR, '#user_id')  # 아이디 입력란 ID 확인 필요
    id_input.send_keys(user_id)

    # 비밀번호 입력
    pw_input = driver.find_element(By.CSS_SELECTOR, "#user_password")  # 비밀번호 입력란 ID 확인 필요
    pw_input.send_keys(user_pw)

    # 로그인 버튼 클릭
    login_btn = driver.find_element(By.CSS_SELECTOR, "#loginFrm > div.check > a > button")  # 로그인 버튼 ID 확인 필요
    login_btn.click()

    print("로그인 성공!")

    # 페이지 유지 시간 (예제용)
    time.sleep(10)

except Exception as e:
    print("오류 발생:", e)

finally:
    # 웹드라이버 종료
    driver.quit()
