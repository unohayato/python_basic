from logging import getLogger, StreamHandler, FileHandler,Formatter, DEBUG, ERROR, INFO

formatter = Formatter('[%(levelname)s] %(asctime)s - %(message)s (%(filename)s)')
logger = getLogger(__name__)

handler = FileHandler('log2.txt')
handler.setLevel(DEBUG)
handler.setFormatter(formatter)

error_handler = FileHandler('error.txt')
error_handler.setLevel(ERROR)
error_handler.setFormatter(formatter)

logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.addHandler(error_handler)


logger.debug('入力値は1000です')
logger.info('プログラムが開始しました')
logger.warning('ファイルの容量が299GBを越えました')
logger.error('ファイルが存在していません')


