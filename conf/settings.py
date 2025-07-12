from decouple import config


ENV = config('ENV', cast=str, default='PROD')
FERNET_KEY = config('FERNET_KEY', cast=lambda s: s.encode())  # a byte type
LOG_LEVEL = config('LOG_LEVEL', cast=str, default='INFO')


class Timeouts:
    VERY_SHORT: int = 3
    SHORT: int = 10
    DEFAULT: int = 30
    LONG: int = 120
    VERY_LONG: int = 300
