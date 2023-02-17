import traceback

try:
  result = 1 / 0
  print(result)
except ZeroDivisionError:
  print('---トレースバックを開始---')
  t = traceback.format_exc()
  print(t)
  print('---トレースバックを終了---')
  
  