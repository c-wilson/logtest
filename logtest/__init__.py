import sys
import os
import logging
import logtest.module1


# setting
_log_fmt_string = '%(asctime) -23s %(name)-23s %(levelname)-8s %(message)s'
_log_datefmt = "%Y-%m-%dT%H:%M:%S"
logging.basicConfig(stream=sys.stderr, level=logging.INFO, format=_log_fmt_string, datefmt=_log_datefmt)

b = module1.MyClass()