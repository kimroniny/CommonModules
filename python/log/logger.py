import logging, os
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter(
    '%(asctime)s %(name)s %(funcName)s %(levelname)s (%(lineno)d) %(message)s'
)
logFile = __file__+'.log'
if os.path.exists(logFile):
    os.remove(logFile)
my_handler = RotatingFileHandler(
    logFile, 
    mode='a', 
    maxBytes=5*1024*1024, 
    backupCount=5, 
    encoding='utf-8', 
    delay=0
)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)

logger = logging.getLogger(__name__) # 如果没有__name__那么调取的就是root logger, 即所有的消息
logger.addHandler(my_handler)