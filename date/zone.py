from datetime import timezone, timedelta, datetime

JST = timezone(timedelta(hours=+9))
ret = datetime(2020, 1, 1, tzinfo=JST)
print(ret)