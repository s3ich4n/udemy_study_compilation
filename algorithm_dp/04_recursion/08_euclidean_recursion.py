def gcd(a, b):
    """ 

    베이스케이스를 잘 살피자 (리턴 케이스같다)
    아니면 재귀하도록 하는 케이스를 잘 살피자

    어떻게 보면 점화식을 세우는 것과 크게 다를 바 없어보인다
    """
    if a % b == 0:
        return b

    return gcd(b, a % b)


print(gcd(45, 10))


def gcd_iter(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b


print(gcd_iter(12355, 21394))
