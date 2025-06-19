import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'#크롤링할 사이트 url 설정

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.basic1')#첫번째 요소
    titles = ul.select('li > dl > dt > a')#부가 요소 경로
    for title in titles:#요소가 여러개이므로 for문 이용
        print(title.get_text())

else :
    print(response.status_code)
