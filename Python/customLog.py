import logging
import os
# Define standard logger common for all modules


class Logger:
    def __init__(self, logger_name, logfile=None):
        self._logger = logging.getLogger(logger_name)
        log_dir = os.path.join(os.getcwd(), ".log")
        # print "log dir: %s", log_dir
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        if logfile is None:
            self._logfile = os.path.join(log_dir, logger_name+'.log')
        else:
            self._logfile = logfile
        print "logfile: ", self._logfile
        if os.path.isfile(self._logfile):
            os.remove(self._logfile)
        self._file_handler = logging.FileHandler(self._logfile)
        self._console_handler = logging.StreamHandler()
        self._formatter = logging.Formatter("%(levelname)s - %(message)s")
        self._file_handler.setFormatter(self._formatter)
        self._console_handler.setFormatter(self._formatter)
        self._logger.addHandler(self._console_handler)
        self._logger.addHandler(self._file_handler)
        # Default levels

        self._logger.setLevel(logging.DEBUG)
        self._file_handler.setLevel(logging.DEBUG)
        self._console_handler.setLevel(logging.WARNING)

    def set_logger_level(self, level):
        self._logger.setLevel(level)

    def set_file_handler_level(self, level):
        self._file_handler.setLevel(level)

    def set_console_handler_level(self, level):
        self._console_handler.setLevel(level)

    def get_logger(self):
        return self._logger
