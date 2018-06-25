import sys
import os
import logging
from logtest import module1, mod2


# setting
_log_fmt_string_save = '%(asctime) -23s %(name)-23s %(levelname)-8s %(message)s'
_log_fmt_string_console = '%(asctime) -23s % (levelname) -8s %(message)s'
_log_datefmt = "%Y-%m-%dT%H:%M:%S"
# logging.basicConfig(stream=sys.stderr, level=logging.INFO, format=_log_fmt_string, datefmt=_log_datefmt)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# b = module1.MyClass()