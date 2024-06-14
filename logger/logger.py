import os
import logging
from logger import settings


class Logger:

    def __init__(self, logger_name, level=logging.DEBUG):
        self.logger_name = logger_name
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level)

        formatter = logging.Formatter(settings.FORMAT)
        log_directory = os.path.abspath("../logs/")
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        log_file_path = os.path.join(log_directory, f"{logger_name}.log")

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        stdout_handler = logging.StreamHandler()
        stdout_handler.setFormatter(formatter)
        self.logger.addHandler(stdout_handler)

    def error(self, msg):
        # Place for connection to store logs in remote database
        self.logger.error(msg, extra={'unit': self.logger_name})

    def info(self, msg):
        # Place for connection to store logs in remote database
        self.logger.info(msg, extra={'unit': self.logger_name})

    def debug(self, msg):
        # Place for connection to store logs in remote database
        self.logger.debug(msg, extra={'unit': self.logger_name})
