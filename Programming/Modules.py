import random
from collections import deque
from datetime import datetime

qq = deque([])
c=1
for x in range(100):
    i = random.random()
    if i <= 0.8:
        qq.append(c)
        c += 1
    elif i > 0.8:
        qq.popleft()
        c += 1
    elif 0.5 <= i < 0.8:
        i = random.random()
        if i <= 0.5:
            qq.append(c)
            c += 1
        else:
            qq.popleft()
            c += 1
    print(qq)
"""
now = datetime.today()
print(now.strftime("%Y-%m-%d ----- %B"))
xmas = datetime(2025, 12, 25, 00)
dday = xmas - now
print(dday)
"""