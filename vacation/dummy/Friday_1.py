import random
import time
import os

def even_odd():
    """짝수 홀수 구별"""
    try:
        number = int(input("\n숫자를 입력해주세요 ex) 3: "))
        if number % 2 == 0:
            print("\n이 숫자는 짝수입니다.")
        else:
            print("\n이 숫자는 홀수입니다.")
    except ValueError:
        print("\n올바른 형태로 입력해주세요.")

def times_table():
    """구구단 출력"""
    try:
        number = int(input("\n보고싶은 구구단의 숫자를 입력해주세요 (범위는 정수 1~9): "))
        if 0 < number < 10:
            for x in range(1,10):
                print(f"{number} x {x} = {number*x}")
        else:
            print("\n1~9사이의 정수를 입력해주세요.")

    except ValueError:
        print("\n올바르지 않은 입력 값입니다.")

def max_list(list_):
    """리스트에서 최댓값을 찾아서 순서와 함께 출력"""
    try:
        find_value = max(list_)
        find_index = [i for i, x in enumerate(list_) if x == max(list_)] #list_.index(max(list_))
        print(f"\n이 리스트 요소의 최댓값은 {find_value}이고, 그 값의 순서는 {find_index[0]}입니다.")
    except ValueError:
        print("\nlist를 인자로 넣어주세요")

def calculator():
    """숫자형 인자 2개를 받아서 계산"""
    try:
        numbers = input("\n계산하고자 하는 두 수를 입력해주세요 ex) 3, 4: ").split(",")
        option = int(input("\n사용하고자 하는 기능에 해당하는 번호를 입력해주세요"
                           "\n1번: 덧셈(a+b) 2번: 뺄셈(a-b) 3번: 곱셈(axb) 4번: 나눗셈(a/b), ex) 1: "))
        if option == 1:
            print("%0.4f" %(float(numbers[0]) + float(numbers[1])))
        elif option == 2:
            print("%0.4f" %(float(numbers[0]) - float(numbers[1])))
        elif option == 3:
            print("%0.4f" %(float(numbers[0]) * float(numbers[1])))
        elif option == 4:
            print("%0.4f" %(float(numbers[0]) / float(numbers[1])))
        else:
            print("\n올바른 옵션 번호가 아닙니다.")

    except ValueError:
        print("\n올바른 값을 입력해주세요.")

def palindrome_check(str_):
    """회문 구별"""
    try:
        test = str_.split()
        if test[0] == test[-1]:
            print("\n이 문자열은 회문입니다!")
        else:
            print("\n이 문자열은 회문이 아닙니다.")
    except TypeError:
        print("\n문자열을 입력해주세요.")

def make_lotto_numbers():
    """로또 번호 생성기"""
    numbers = list(range(1, 46))
    lotto_numbers = []
    #random.sample(range(1, 46), 6) 한 줄이면 중복 없는 6개를 바로 얻음
    for x in range(6):
        lotto_numbers.append(random.choice(numbers))
    lotto_numbers = set(lotto_numbers)
    if len(lotto_numbers) < 6:
        while len(lotto_numbers) < 6:
            lotto_numbers.add(random.choice(numbers))
            if len(lotto_numbers) == 6:
                break
        print(f"\n{sorted(lotto_numbers)}")
    else:
        print(f"\n{sorted(lotto_numbers)}")

def word_counter():
    """각각의 단어가 몇번 반복 되는지 딕셔너리 형태로 출력"""
    #파이썬 3.7+에서는 collections.Counter를 활용하면 한 줄:
    #from collections import Counter
    #counts = Counter(word.split())
    word = input("\n각 단어의 개수를 세고자 하는 문자열을 입력해주세요: ")
    word_split = word.split()
    count = {}
    for x in word_split:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    print(count)

def celsius_fahrenheit():
    """섭씨 온도와 화씨 온도간의 변환"""
    try:
        degree = float(input("\n변환시키고자 하는 온도값을 입력해주세요 ex) 3.5: "))
        option = int(input("\n이용하고자 하는 옵션에 해당하는 번호를 입력해주세요 ex) 2"
                           "\n1번: 섭씨 -> 화씨, 2번: 화씨 -> 섭씨: "))
        if option == 1:
            print(f"\n섭씨 {degree}°C는 화씨 {(degree*9/5)+32:0.4f}°F 입니다.")
        elif option == 2:
            print(f"\n화씨 {degree}°F는 섭씨 {(degree-32)*5/9:0.4f}°C 입니다.")
        else:
            print("\n올바른 옵션 번호를 입력해주세요.")
    except ValueError:
        print("\n숫자를 입력해주세요.")

def memo():
    path = ("%s" %os.getcwd())
    contents = input("memo에 적을 내용을 입력해주세요: ")
    time_ = "\nInput_Time: %s" %time.ctime()
    with open("%s\\memo.txt" %path, "w") as f:
        f.write(contents)
        f.write(time_)

while True:
    memo()
    end_or_not = input("\n프로그램을 종료하려면 q를 입력해주시고" #flag
                       "\n그렇지 않다면 아무값을 입력해주세요: ")
    if end_or_not == 'q':
        break
    else:
        continue