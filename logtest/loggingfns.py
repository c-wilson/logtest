"""Logging functions"""

import logging
import sys

# log settings
_file_format = '%(asctime) -23s %(name)-23s %(levelname)-8s %(message)s'
_console_format = '%(asctime) -23s %(levelname)-8s %(message)s'
_date_fmt = "%Y-%m-%dT%H:%M:%S"

CONSOLE_HANDLER = None
FILE_HANDLER = None


def setup_console_logging(level=logging.INFO, format=_console_format, date_fmt=_date_fmt):
    """Sets up logging to the console.

    Parameters
    ----------
    level : int
        Logging level, usually specified with logging.INFO, logging.WARNING, etc
    format : str
        String specifying logging format (see Python docs)
    date_fmt : str
        String specifying date format (see Python docs)
    """

    global CONSOLE_HANDLER
    rootlogger = logging.getLogger()

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    formatter = logging.Formatter(format, date_fmt)
    handler.setFormatter(formatter)

    rootlogger.setLevel(min((rootlogger.level, level)))
    # root level must be <= the handler level for the handler to receive the events.

    if CONSOLE_HANDLER is not None:
        rootlogger.removeHandler(CONSOLE_HANDLER)
    CONSOLE_HANDLER = handler
    rootlogger.addHandler(handler)

    return


def setup_file_logging(filename, level=logging.INFO, format=_file_format, date_fmt=_date_fmt, write_mode='a'):
    """Sets up writing logging to filesystem.

    Parameters
    ----------
    filename : str
        Path to the file you want to write.
    level : str
        Logging level, usually specified with logging.INFO, logging.WARNING, etc
    format : str
        String specifying logging format (see Python docs)
    date_fmt : str
        String specifying date format (see Python docs)
    write_mode : str
        Mode to write file. Default is 'a' for append. See Python file stream documentation for other options.
    """
    global FILE_HANDLER
    rootlogger = logging.getLogger()

    handler = logging.FileHandler(filename, mode=write_mode)
    handler.setLevel(level)
    formatter = logging.Formatter(format, date_fmt)
    handler.setFormatter(formatter)

    rootlogger.setLevel(min((rootlogger.level, level)))
    # root level must be <= the handler level for the handler to receive the events.

    if FILE_HANDLER is not None:
        rootlogger.removeHandler(FILE_HANDLER)
    FILE_HANDLER = handler
    rootlogger.addHandler(handler)

    return
