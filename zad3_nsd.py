"""
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""
import sympy, math, numpy, pytest

def prost(n):
    """
    проверка числа на простоту

    :param n: число
    :return: true / false
    """
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
    return True

def nsd(n):
    """
    ищет самый большой простой делитель

    :param n: число
    :return: самый большой простой делитель
    """
    # n = numpy.int64(abs(n))
    # if n < 4:
    #     return n
    # max = int(math.sqrt(n+10))
    # for i in reversed(range(2, max)):
    #     if (n % i == 0) and (sympy.isprime(i)):
    #         return i
    # print(math.sqrt(n))
    # s = 2
    # while True:
    #     if (n % s == 0):
    #         if (n // s == 1):
    #             return s
    #         n = n / s
    #     s += 1
    s = 2
    while s * s < n:
        while n % s == 0:
            n = n // s
        s += 1
    if n % s == 0:
        n = n // s
    return n



@pytest.mark.parametrize('a,b', [(13195, 29), (600851475143, 6857), (600851475141, 16716787)])
class TestNsd:
    def test_nsd1(self, a, b):
        assert nsd(a) == b, f'error {b}'

    # def test_nsd2(self):
    #     assert nsd(a) == 6857, 'error 600851475143'
    #
    # def test_nsd3(self):
    #     assert nsd(600851475141) == 16716787, 'error 600851475141'


print(nsd(100))
print(nsd(600851475141))
print(nsd(13195))
print(nsd(22))
print(nsd(600851475143))