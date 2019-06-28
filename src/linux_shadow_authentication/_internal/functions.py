"""This script contains the main authentication and hash generation functions"""

import subprocess
from linux_shadow_authentication._internal.classes import ShadowHash
from linux_shadow_authentication._internal.enums import Algorithm
from linux_shadow_authentication._internal.validations import (
    validate_system_requirements_first
)

from linux_shadow_authentication._internal.exceptions import (
    # Exceptions
    InvalidArgumentType,

    # Exception Messages
    MESSAGE_INVALID_ALGORITHM_TYPE,
    MESSAGE_INVALID_SALT_TYPE,
    MESSAGE_INVALID_TEXT_TYPE,
    MESSAGE_INVALID_USERNAME_TYPE,
    MESSAGE_INVALID_HASHED_PASSWORD_TYPE,
    MESSAGE_INVALID_PASSWORD_TYPE
)


def _generate_openssl_hash(algorithm: Algorithm, salt: str, text: str) -> str:
    """
    Internal function that generates a Hash using the openssl program.

    :param algorithm: A valid hashing algorithm to be used
    :param salt: The salt added when generating the hash
    :param text: The text to be hashed
    :return: A hashed string
    :raises InvalidArgumentType:
    """
    if not isinstance(algorithm, Algorithm):
        raise InvalidArgumentType(MESSAGE_INVALID_ALGORITHM_TYPE)
    if not isinstance(salt, str):
        raise InvalidArgumentType(MESSAGE_INVALID_SALT_TYPE)
    if not isinstance(text, str):
        raise InvalidArgumentType(MESSAGE_INVALID_TEXT_TYPE)

    return subprocess.check_output(
        "echo {text} | openssl passwd -{algorithm} -salt {salt} -stdin".format(
            text=text,
            algorithm=algorithm.value,
            salt=salt
        ),
        shell=True
    ).decode("utf-8")[:-1]


def _get_user_password_hash_from_shadow_file(username: str) -> str:
    """
    Internal function that retrieves the password hash from a Linux user.

    :param username: A valid hashing algorithm to be used
    :return: A the hashed password string
    :raises InvalidArgumentType:
    """
    if not isinstance(username, str):
        raise InvalidArgumentType(MESSAGE_INVALID_USERNAME_TYPE)

    return subprocess.check_output(
                "cat /etc/shadow | grep {user}".format(user=username),
                shell=True
            ).decode("utf-8").split(":")[1]


@validate_system_requirements_first
def generate_openssl_hash(algorithm: Algorithm, salt: str, text: str) -> str:
    """
    Generates a Hash using the openssl program.

    :param algorithm: A valid hashing algorithm to be used
    :param salt: The salt added when generating the hash
    :param text: The text to be hashed
    :return: A hashed string
    :raises PrerequisiteException, InvalidArgumentType:
    """
    if not isinstance(algorithm, Algorithm):
        raise InvalidArgumentType(MESSAGE_INVALID_ALGORITHM_TYPE)
    if not isinstance(salt, str):
        raise InvalidArgumentType(MESSAGE_INVALID_SALT_TYPE)
    if not isinstance(text, str):
        raise InvalidArgumentType(MESSAGE_INVALID_TEXT_TYPE)

    return _generate_openssl_hash(algorithm=algorithm, salt=salt, text=text)


@validate_system_requirements_first
def validate_system_user_with_hash(username: str, hashed_password: str) -> bool:
    """
    Validates the given credentials for a user in the system using a hashed password.

    :param username: The user to be validated in the system
    :param hashed_password: The password hash to be used to compare the credentials
    :return: true if credentials are valid, false if they are not.
    :raises PrerequisiteException, InvalidArgumentType, InvalidArgumentFormat:
    """
    if not isinstance(username, str):
        raise InvalidArgumentType(MESSAGE_INVALID_USERNAME_TYPE)

    if not isinstance(hashed_password, str):
        raise InvalidArgumentType(MESSAGE_INVALID_HASHED_PASSWORD_TYPE)

    shadow_object = ShadowHash(hashed_password)
    return shadow_object.equals(_get_user_password_hash_from_shadow_file(username))


@validate_system_requirements_first
def validate_system_user_with_string_password(username: str, password: str) -> bool:
    """
    Validates the given credentials for a user in the system using a string password.

    :param username: The user to be validated in the system
    :param password: The password to be used to compare the credentials
    :return: true if credentials are valid, false if they are not
    :raises PrerequisiteException, InvalidArgumentType, InvalidArgumentFormat:
    """
    if not isinstance(username, str):
        raise InvalidArgumentType(MESSAGE_INVALID_USERNAME_TYPE)
    if not isinstance(password, str):
        raise InvalidArgumentType(MESSAGE_INVALID_PASSWORD_TYPE)

    shadow_object = ShadowHash(_get_user_password_hash_from_shadow_file(username))
    return shadow_object.equals(_generate_openssl_hash(
                                    algorithm=shadow_object.algorithm,
                                    salt=shadow_object.salt,
                                    text=password)
                                )
