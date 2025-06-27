import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)

print("start")

threads = []
for i in range(5):
  t = threading.Thread(target=long_task)  #thread 생성
  threads.append(t)

for t in threads:
  t.start()  #thread 실행

for t in threads:
  t.join()  #thread 종료까지 대기

print("end")
#collab 확인하자.