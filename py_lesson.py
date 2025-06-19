import random
flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookies"]
#가짜 투표수 제작
def make_votes(num_votes):
  votes = []
  for x in range(num_votes):
    votes.append(random.choice(flavors))
  return votes
#투표 결과 분석 (가장 투표를 많이 받은 맛, 투표를 받은 맛의 종류와 이름, 투표에 참여한 총 인원 수)
def analyze_votes(ballots):
  unique_flavors = set()
  counts = {}
  for taste in ballots:
    unique_flavors.add(taste)
    counts[taste] = counts.get(taste, 0) + 1
  for taste in counts:
    if counts[taste] == counts[max(counts)]:
      top_flavor = taste
      top_count = counts[taste]
  return (top_flavor, unique_flavors, len(ballots), top_count)
#형식에 맞게 출력
def print_output(top_flavor, unique_flavors, total, top_count):
  print (f"Total votes: {total}\n"
          f"Flavors ({len(unique_flavors)} types): {', '.join(unique_flavors)}\n"
          f"Top flavor: {top_flavor} (counts: {top_count})")
#입력값 받기 & 오류 방지
while True:
    num = input("투표에 참여하는 학생의 수를 입력해주세요(프로그램을 종료하려면 'v'키를 입력하세요):")
    try:
        if num == 'v':
            break
        print_output(*analyze_votes(make_votes(int(num))))

    except:
        print("잘못된 입력 방식입니다.")
        continue