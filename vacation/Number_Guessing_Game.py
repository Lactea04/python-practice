#🎯 숫자 맞추기 게임 (Number Guessing Game)
#🧩 기능 설명:
#컴퓨터가 1부터 100 사이의 숫자 중 하나를 무작위로 선택합니다.

#사용자는 그 숫자를 맞출 때까지 계속 입력합니다.

#컴퓨터는 사용자의 입력이 정답보다 높은지, 낮은지를 알려줍니다.

#정답을 맞추면 몇 번 만에 맞췄는지 출력합니다.

#수정 버전은 collab에서 확인
import random



quiz = random.choice(range(1, 101))
count = 0

class MyError(Exception):
    pass



def compare_num(quiz, num):
    global count
    if quiz == num:
        count += 1
        end()
    elif quiz > num:
        count += 1
        print(f"이 숫자는 입력하신 숫자보다 큽니다! (현재 시도한 횟수: {count}회)\n")
    elif quiz < num:
        count += 1
        print(f"이 숫자는 입력하신 숫자보다 작습니다! (현재 시도한 횟수: {count}회)\n")

def end():
    message = input(f"정답입니다! 정답을 맞추기까지 시도한 횟수는 {count}회 입니다. 종료하시려면 'v'를 입력해주세요.:")
    if message == "v":
        raise MyError()


while True:
    try:
        num = int(input(" 이 숫자는 몇 일까요? 추측하신 숫자를 입력해주세요:"))
        compare_num(quiz, num)
    except ValueError:
        print("올바르지 않은 형식의 입력값입니다!")
        continue
    except MyError:
        break

