import traceback
import trace2
from logging import getLogger, FileHandler, DEBUG

logger = getLogger(__name__)
handler = FileHandler('log.txt')
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

def main():
  try:
    trace2.func1()
  except Exception:
    t = traceback.format_exc()
    logger.debug(t)
    
if __name__ == '__main__':
  main()