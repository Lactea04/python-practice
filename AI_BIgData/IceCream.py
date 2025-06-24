import random
flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookies"]
#가짜 투표수 제작
def make_votes(num_votes):
  votes = []
  for x in range(num_votes):
    votes.append(random.choice(flavors))
  return votes
#투표 결과 분석 (가장 투표를 많이 받은 맛, 투표를 받은 맛의 종류와 이름, 투표에 참여한 총 인원 수, 투표 결과)
def analyze_votes(ballots):
  unique_flavors = set()
  counts = {}
  #unique_flavors = set(ballots) 한 번에 할 수 있긴 함
  for taste in ballots:
    unique_flavors.add(taste)  #13줄 참고
    counts[taste] = counts.get(taste, 0) + 1
#top_flavor 중복일 때 처리 및 받은 투표 수(top_count) 표시
  top_flavor = []
  for value in counts.items():
      if value[1] == counts[max(counts,key=lambda x:counts[x])]:
          top_flavor.append(value[0])
          top_count = value[1]
  #top = counts[max(counts, key=lambda x:counts[x])]
  #top_flavor = [key for key, value in counts.items() if value == top] <-GPT 코드
  #top_count = counts[max(counts,key=lambda x:counts[x])]
# 수업 시간에 배웠던 방법
  #top_count = -1
  #top_flavor = []
  #for taste in counts:
  # if top_count < counts[taste]:
  #   top_count = counts[taste]
  #   top_flavor.append(taste)
  # 최소를 찾을 때는 top_count의 값을 가장 큰 값으로 설정
  return (top_flavor, unique_flavors, len(ballots), top_count, counts)
#형식에 맞게 출력
def print_output(top_flavor, unique_flavors, total, top_count, counts):
  print (f"Total votes: {total}\n"
          f"Flavors ({len(unique_flavors)} types): {', '.join(unique_flavors)}\n"
          f"Top flavor: {top_flavor} (counts: {top_count})\nResult: {counts}")
#입력값 받기 & 오류 방지
while True:
        num = input("투표에 참여하는 학생의 수를 입력해주세요(프로그램을 종료하려면 'v'키를 입력하세요):")
        if num == 'v':
            break
        else:
            try:
                num = int(num)
                print_output(*analyze_votes(make_votes(int(num))))
            except:
                print("잘못된 입력 방식입니다.")
                continue