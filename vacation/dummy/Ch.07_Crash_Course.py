#name = input("Hello, what's your name?: ")
#print(f"\nHello, {name}!") 프롬프트 구별해주는게 좋음

#input으로 숫자를 받아올 경우, 문자열로 인식하므로 int()를 사용하자.

#입력한 값이 짝수인지 판별하기
prompt = "I will distinguish between even-number and odd-number."
prompt += "\nPlease input some number:"

#while을 이용하여 리스트내에 여러번 존재하는 요소 제서
#animals = ['cat', 'dog', 'cow', 'duck', 'cat', 'mouse', 'bat', 'cat']
#while 'cat' in animals:
#   animals.remove('cat')


run_check = True

while run_check:
    try:
        number = int(input(prompt))
        if number % 2 == 0:
            print(f"\nIt is even-number!")
        else:
            print(f"\nIt is odd-number!")
        Constant = input("\nif you want to try again please input 'A'! ") #flag
        if Constant == 'A':
            continue
        else:
            run_check = False #break를 사용하지 않고 끝낼 수 있음
    except ValueError:
        print("\nIt is wrong type value, please input correct type value.\n")