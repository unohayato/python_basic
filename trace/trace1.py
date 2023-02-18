import traceback
import trace2

def main():
  trace2.func1()
  
if __name__ == '__main__':
  main()
  

# try:
#   result = 1 / 0
#   print(result)
# except ZeroDivisionError:
#   print('---トレースバックを開始---')
#   t = traceback.format_exc()
#   print(t)
#   print('---トレースバックを終了---')