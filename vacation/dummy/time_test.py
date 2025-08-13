import time
import calendar


a = time.time()

b = time.localtime(a)

c = time.asctime(b)
#print(c)


#print(time.ctime()) #위의 과정 축약 한 것 //항상 현재 시간만 알려줌.
#print(time.strftime("%c", b)) #  %c 날짜와 시간 출력


#d = calendar.prmonth(2025, 6)
#print(d) #특정 연, 월의 달력 출력
#print(calendar.calendar(2025)) # 그해 달력 전체 출력 = calendar.prcal(2025)
#print(calendar.weekday(2025, 6, 27)) #특정 연, 월 ,일의 요일을 숫자값으로 출력 0~6까지 월~일요일 순
#print(calendar.monthrange(2025,6)) #특정 연월의 (시작 요일, 그 달의 일수) 출력
