from logging import getLogger, StreamHandler, Formatter, DEBUG, ERROR, INFO

formatter = Formatter('[%(levelname)s] %(asctime)s - %(message)s (%(filename)s)')
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
handler.setFormatter(formatter)
logger.setLevel(INFO)
logger.addHandler(handler)
logger.info('入力値はxxです')


