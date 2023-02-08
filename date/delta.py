from datetime import datetime, timedelta

d = datetime(2023, 2, 7, 0, 0, 0)
ret = d + timedelta(days=30)
print(ret)