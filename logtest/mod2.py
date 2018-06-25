from logtest import loggingfns
import logging
logger = logging.getLogger(__name__)

def main():
    loggingfns.setup_console_logging()
    loggingfns.setup_file_logging('test2.txt', logging.DEBUG)

    logger.info('Info!')
    logger.debug('DEBUG!')
    return
