from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://www.gachon.ac.kr/kor/3104/subview.do")

time.sleep(3)  # JavaScript 로딩 대기

# 다운로드 버튼 클릭 (예시, 정확한 요소 확인 필요)
try:
    download_button = driver.find_element(By.CSS_SELECTOR, "a.download-btn")  # 정확한 CSS 선택자 확인 필요
    download_button.click()
    time.sleep(5)  # 파일 다운로드 대기
except Exception as e:
    print("다운로드 버튼 클릭 실패:", e)

# 현재 HTML 확인
print(driver.page_source)

driver.quit()
