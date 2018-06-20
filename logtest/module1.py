import logtest
import logging

logger = logging.getLogger(__name__)


def main():
    logger.info('Good afternoon!')
    logger.debug('You bastard!')


def main2():
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