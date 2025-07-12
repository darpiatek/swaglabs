from typing import Union

from cryptography.fernet import Fernet

from conf.settings import FERNET_KEY


def encrypt(value: bytes, key: bytes = None) -> bytes:
    """
    Returns data encrypted with a key
    :param value: Value to be encrypted
    :param key: Key for encryption
    :return: Encrypted value
    """
    assert isinstance(value, bytes), "Token is not bytes type"
    return Fernet(key).encrypt(value)


def decrypt(value: bytes, key: bytes = None) -> str:
    """
    Returns data decrypted with a key
    :param value: Value to be decrypted
    :param key: Key for decrypting
    :return: Decrypted value
    """
    assert isinstance(value, bytes), "Token is not bytes type"
    return Fernet(key).decrypt(value).decode()


def create_new_key() -> bytes:
    """
    Creates new key for decryption
    :return: Key
    """
    return Fernet.generate_key()


def encode_if_str(value: Union[bytes, str]) -> bytes:
    """
    Encodes if value is a string
    :param value: Value to be encoded
    :return: Key
    """
    if isinstance(value, str):
        return value.encode()
    return value


def encrypt_value(value: Union[bytes, str]) -> bytes:
    """
    Encrypt value with a key
    :param value: Value to be encrypted
    :return: Encrypted value
    """
    return encrypt(encode_if_str(value), FERNET_KEY)


def decrypt_value(value: Union[bytes, str]) -> str:
    """
    Decrypt value with a key
    :param value: Value to be decrypted
    :return: Decrypted value
    """
    return decrypt(encode_if_str(value), FERNET_KEY)
