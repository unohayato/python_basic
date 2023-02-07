from datetime import datetime

n = datetime.now()
print(n)
print(n.year, n.month, n.day)
print(n.hour, n.minute, n.second, n.microsecond)

d1 = datetime(2023, 2, 7)
d2 = datetime(2023, 2, 5)
ret = d1 - d2
print(ret.days)