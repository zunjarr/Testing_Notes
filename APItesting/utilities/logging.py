import logging
import logging_actions

logger = logging.getLogger(__name__)     # __name__ will print test case name

fileHandlerObj = logging.FileHandler('logfile.log')
formatterObj = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
fileHandlerObj.setFormatter(formatterObj)

logger.addHandler(fileHandlerObj)    # fileHandler(File location) object need to pass this method, in which file need to print

logger.setLevel(logging.INFO)
logger.debug('Debug statement is printed')
logger.info('Information statement')
logger.warning('Something is in warning mode')
logger.error('Major error has occurred')
logger.critical('Critical issue')

