from datetime import datetime, timedelta

d = datetime(2020, 12, 25, 3, 0, 0)
ret = d + timedelta(days=10)
print(ret)