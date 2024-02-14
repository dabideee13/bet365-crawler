import os
import logging
from typing import Optional
from datetime import datetime


class CustomLogger:
    _instances = {}
    _time_logger = None
    _start_time = None

    def __new__(cls, name: Optional[str] = None):
        if name not in cls._instances:

            # Create a directory for today's date
            today_date = datetime.now().strftime('%m_%d_%Y')
            daily_logs_path = os.path.join(os.getcwd(), "logs", today_date)
            os.makedirs(daily_logs_path, exist_ok=True)

            # Create a new directory for the current run inside the today's directory
            run_time = datetime.now().strftime('%H_%M_%S')
            run_logs_path = os.path.join(daily_logs_path, run_time)
            os.makedirs(run_logs_path, exist_ok=True)

            # Create a log file for the current spider inside the run's directory
            log_file = f"{name}.log"
            log_file_path = os.path.join(run_logs_path, log_file)

            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")

            # Handler for writing to file
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            # Handler for writing to console
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            cls._instances[name] = logger

            if not cls._time_logger:
                cls._init_time_logger()

        return cls._instances[name]

    @classmethod
    def _init_time_logger(cls):
        time_logs_path = os.path.join(os.getcwd(), "logs", "time")
        os.makedirs(time_logs_path, exist_ok=True)

        log_file = "time_logs.log"
        log_file_path = os.path.join(time_logs_path, log_file)

        time_logger = logging.getLogger("TimeLogger")
        time_logger.setLevel(logging.INFO)

        formatter = logging.Formatter("[ %(asctime)s ] - %(message)s")

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        time_logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        time_logger.addHandler(console_handler)

        cls._time_logger = time_logger

    @classmethod
    def log_start_time(cls):
        """Log the start time."""
        if cls._time_logger:
            cls._start_time = datetime.now()
            cls._time_logger.info("Code started running.")

    @classmethod
    def log_end_time(cls):
        """Log the end time."""
        if cls._time_logger and cls._start_time:
            end_time = datetime.now()
            duration = (end_time - cls._start_time).total_seconds() / 60
            cls._time_logger.info("Code finished running.")
            cls._time_logger.info(f"Total duration: {duration:.2f} minutes.")