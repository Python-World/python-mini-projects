from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase
from string import digits
from string import punctuation as spacial
from typing import Iterator

from toolbox import *


class PasswordSecurityLevel:
    a = mixer(digits, lowercase, uppercase, spacial)
    b = mixer(lowercase, uppercase, digits)
    c = mixer(lowercase, uppercase)
    d = mixer(digits, lowercase)
    e = mixer(digits)

    @classmethod
    def get(cls, level: str) -> List:
        """ return level by level title """
        if len(level) == 1:
            return cls.__dict__[level]


def password_generator(source: Iterable = PasswordSecurityLevel.a, lenght: int = 8) -> str:
    password = ''.join(choice(source, lenght))
    return password
