import logging
import logging.config
from pathlib import Path

from conf import path_conf
from conf.settings import LOG_LEVEL

LOG_FORMAT: str = '[%(asctime)s] [%(levelname)s] %(message)s'

class Logger(logging.Logger):
    """Class dedicated for Logger."""

    def scenario(self, message: str, *args, **kwargs) -> None:
        """
        Scenario loger method
        :param message: Message to be recorded
        :return None
        """
        self.info(f'SCENARIO: {message}', *args, **kwargs)

    def precondition(self, message: str, *args, **kwargs) -> None:
        """
        Precondition loger method
        :param message: Message to be recorded
        :return None
        """
        self.info(f'PRECONDITION: {message}', *args, **kwargs)

    def warn(self, message: str, *args, **kwargs) -> None:
        """
        Step loger method
        :param message: Message to be recorded
        :return None
        """
        self.warning(f'WARNING: {message}', *args, **kwargs)

    def step(self, message: str, *args, **kwargs) -> None:
        """
        Step loger method
        :param message: Message to be recorded
        :return None
        """
        self.info(f'STEP: {message}', *args, **kwargs)

    def substep(self, message: str, *args, **kwargs) -> None:
        """
        SubStep loger method
        :param message: Message to be recorded
        :return None
        """
        self.info(f'SUBSTEP: {message}', *args, **kwargs)


def get_logger(name: str = __name__, file_name: str = 'test.log') -> Logger:
    """
    Configures and returns logger
    :param name: Logger name
    :param file_name: Filename of the log
    :return Logger
    """
    logger = Logger(name, level=LOG_LEVEL)
    path_conf.LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_file = path_conf.LOG_DIR / file_name
    Path(log_file).touch()
    f_handler = logging.FileHandler(log_file)
    s_handler = logging.StreamHandler()
    s_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    f_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(f_handler)
    logger.addHandler(s_handler)
    return logger
