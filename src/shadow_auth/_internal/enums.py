"""This script contains the enumerations used in the module"""

import enum


class Algorithm(enum.Enum):
    """
    This Enum contains the valid hashing algorithms for the /etc/shadow file.
    """
    MD5 = "1"
    BLOWFISH_2A = "2a"
    BLOWFISH_2Y = "2y"
    SHA_256 = "5"
    SHA_512 = "6"
