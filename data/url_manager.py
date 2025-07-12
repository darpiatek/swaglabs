import configparser
import os

class UrlManager:
    """Reads URLs from config file"""

    def __init__(self, ini_file: str, env: str):
        self._file_name = ini_file
        self._env = env
        self._config = configparser.ConfigParser()
        if not os.path.exists(self._file_name):
            raise FileExistsError(self._file_name)
        self._config.read(self._file_name)
        if self._env not in self._config.sections():
            raise Exception(f'Configuration for {self._env} does not exist')

    @property
    def urls(self):
        return self._config[self._env]
