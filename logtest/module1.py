import logtest
import logging
import sys

logger = logging.getLogger(__name__)
NEW = False


def main():
    rootlogger = logging.getLogger()
    print(rootlogger)
    filehandler = logging.FileHandler('log.txt', mode='a')
    formatter = logging.Formatter(logtest._log_fmt_string_save, logtest._log_datefmt)
    filehandler.setFormatter(formatter)
    filehandler.setLevel(logging.DEBUG)
    rootlogger.addHandler(filehandler)

    stdouthandler = logging.StreamHandler(sys.stdout)
    stdouthandler.setLevel(logging.INFO)

    rootlogger.addHandler(stdouthandler)

    logger.info('Good afternoon!')
    logger.debug('You bastard!')




def main2():
    global NEW
    print(NEW)
    NEW = True
    logger.info('running main2')
    try:
        65/0
    except ZeroDivisionError as e:
        logger.exception(e)
        pass

class MyClass:
    pass


if __name__ == '__main__':
    main()
    main2()