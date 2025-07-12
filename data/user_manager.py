import configparser
import os

from conf.encrypting import decrypt_value


class UserManager:
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
    def users(self):
        return self._config[self._env]

    def get_user_name(self, user_name):
        return decrypt_value(self._config[self._env][f'{user_name}_username'])

    def get_password(self, user_name):
        return decrypt_value(self._config[self._env][f'{user_name}_password'])