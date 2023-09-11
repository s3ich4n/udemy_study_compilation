import collections
from functools import lru_cache
from itertools import permutations, combinations


@lru_cache(maxsize=128)
def perm(counter: int):
    if counter == 1:
        return len(list(combinations([_ for _ in range(counter * 2)], r=2)))
    else:
        return len(list(combinations([_ for _ in range(counter * 2)], r=2)))


def get_perm(counter: int):
    if counter == 1:
        return perm(1)
    
    else:
        a = perm(counter)
        return a


print(get_perm(2))
print(get_perm(3))
