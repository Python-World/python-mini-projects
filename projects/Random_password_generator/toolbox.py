from random import choices
from typing import Iterable, List


def mixer(*iterators: Iterable) -> List:
    """ merge itrators to one itrator """
    return list(value for row in zip(*iterators) for value in row)


def choice(iterator: Iterable, count: int) -> List:
    """ shortcut for random.choices """
    return choices(iterator, k=count)
