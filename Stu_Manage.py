#📝 과제 제목: 학생 성적 관리 시스템
#🎯 목표
#딕셔너리를 활용해 여러 학생의 과목별 성적을 저장하고, 평균 성적 계산 및 성적 조회 기능을 구현합니다.

#📌 요구사항
#학생 등록
#사용자가 학생 이름을 입력하면, 해당 학생을 딕셔너리에 추가합니다.

#성적 입력
#학생 이름과 과목 이름, 점수를 입력하면 해당 정보를 딕셔너리에 저장합니다.

#예: "홍길동", "수학", 85

#전체 학생 목록 출력
#모든 학생 이름을 출력합니다.

#특정 학생의 성적 조회
#학생 이름을 입력하면, 해당 학생의 과목별 성적과 평균을 출력합니다.

#전체 평균 성적 출력
#모든 학생의 모든 과목 평균을 출력합니다.
stu = {}
def add_name():
    if menu == "1":
        stu_name = str(input("추가할 학생을 입력해주세요 ex)홍길동:"))
        stu[stu_name] = {}
def add_point():
    if menu == "2":
        stu_name = str(input("성적을 입력할 학생의 이름을 입력해주세요 ex)홍길동:"))
        if stu_name in stu:
            subject = input("입력할 성적의 과목명을 입력해주세요 ex)국어:")
            point = input("해당 과목의 성적을 입력해주세요 ex)89:")
            stu[stu_name][subject] = point
        else:
            print("해당 학생은 등록이 안 되어 있으니 메뉴에서 1번 옵션을 활용하여 등록해주세요.")
def show_stuList():
    if menu == "3":
        for name in stu:
            print(name)
def show_stu_point():
    if menu == "4":
        stu_name = input("성적을 확인하고자 하는 학생의 이름을 입력해주세요. ex)홍길동:")
        if stu_name in stu:
            print(stu[stu_name])
        else:
            print("해당 학생은 등록 되어있지 않습니다.")
def check_dic():
    print(stu)
def total_score_average():
    if menu == "6":
        total = 0
        num = []
        for scores in stu.values():
            for score in scores.values():
                total += int(score)
                num.append(scores)
        if len(num) > 0:
            avg = int(total) / len(num)
            print(avg)
        else:
            print("등록된 과목이 없습니다.")
while True:
    menu = input("사용하고자 하는 옵션에 해당하는 번호를 입력해주세요(1: 학생 등록 2: 성적 입력 3: 전체 학생 목록 출력 \n4: 특정 학생 성적 조회 5: 전체 정보 확인 6: 전체 평균. 종료하시려면 아무 키를 입력해주세요. ):")
    if menu not in ["1", "2", "3", "4", "5", "6"]:
        break
    else:
        add_name()
        add_point()
        show_stuList()
        show_stu_point()
        check_dic()
        total_score_average()


