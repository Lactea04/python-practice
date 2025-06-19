from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 열지 않음
driver = webdriver.Chrome(options=options)

# 사이트 접속
url = "https://www.gachon.ac.kr/kor/3104/subview.do"
driver.get(url)

# 페이지가 완전히 로딩될 때까지 대기
time.sleep(5)  # 필요하면 10초 이상 설정

# 현재 페이지 HTML 출력 (파일 링크 확인용)
print(driver.page_source)

driver.quit()
