import time
import calendar


a = time.time()

b = time.localtime(a)

print(b)
c = calendar.prmonth(2025, 6)
print(c)