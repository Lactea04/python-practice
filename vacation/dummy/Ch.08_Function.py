#docstring으로 함수에 대하여 설명 (" 3개를 이용하여 표시)

def add(a,b):
    """a, b를 더하여 값을 출력"""
    result = a+b
    return result

#8-7 음악 앨범 만들기

def make_album(name, title, number = None): #앨범 만들기 함수
    """음악가의 이름, 앨범 제목, 수록곡 숫자(선택사항)를 받아와 딕셔너리 형태로 출력"""
    if number == None: #수록곡 숫자를 입력받지 않았을 경우 2개의 인자만 딕셔너리에 저장
        album = {"Musician's_Name" : str(name), 'Album_Title' : str(title)}
    else:
        album = {"Musician's_Name" : str(name), 'Album_Title' : str(title),
                 'The_Number_Of_Songs_In_Album' : number}
    return album
"""
while True: #프로그램 작동
    try:
        album_information = input("앨범과 관련된 정보를 입력해주세요 \n" 
                              "(FORM: 음악가 이름, 앨범 제목, 앨범에 수록된 곡의 개수) \n"
                              "(ex: Mrs.Green Apple, Lilac, 1): ") #prompt (str_type)
        analyzed_information = album_information.split(",") # 함수에 입력할 수 있는 형태로 변환
        result = make_album(*analyzed_information)
        print("\n%s" %result) # 결과 출력

        message = input("\n 프로그램을 종료하려면 q를 눌려주시고 계속 진행하시려면 아무 문자나 입력해주세요: ") #flag
        if message == 'q':
            break
        else:
            print("\n")
            continue

    except TypeError:
        print("올바르지 않은 입력 형식입니다! 예시에 맞는 형식으로 입력해주세요! \n")
        continue
""" #원래는 '#'으로 주석 처리해야 하지만, 임시방편으로 """로 할 수는 있음, 그러나 완벽한 주석 처리는 아님으로 주의

#**는 키-값 쌍을 받아옴
'''
def user_profile(first, last, **user_info):
    user_info['first'] = first
    user_info['last'] = last

    print(user_info) 

user_profile('Kim', 'Taegyun', age = 22, height = 175)
#{'age': 22, 'height': 175, 'first': 'Kim', 'last': 'Taegyun'}
'''
#모듈을 as로 별칭 부여
import math as m
from math import sin as s
print(m.pi)
print(s(m.pi/2))
#3.141592653589793
#1.0
