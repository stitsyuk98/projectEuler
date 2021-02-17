"""
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""
def fib(i, j=1, np=1, ns=1):
    if i < 1:
        return 0
    if ns > 4000000:
        return ns
    if i == j:
        return ns
    return fib(i, j+1, ns, np+ns)

def sum_fib(n):
    sum = 0
    i = 1
    n_fib = 1
    while (n_fib < 4000000) and (n_fib <= n):
        n_fib = fib(i)
        if (n_fib < 4000000) and (n_fib <= n):
            if n_fib % 2 == 0:
                print(n_fib)
                sum += n_fib
        else:
            return sum
        i += 1
    return sum


class TestSumFib:
    def test_sum_fib1(self):
        assert sum_fib(100) == 44, 'test 100 == 44 error'

    def test_sum_fib2(self):
        assert sum_fib(4000) == 3382, 'test 4000 == 3382  error'

    def test_sum_fib3(self):
        assert sum_fib(-1) == 0, 'test -1 == 0  error'

# print(fib(2))
# print(sum_fib(2))

# не мой код, но прикольно было бы понять, что тут происходит
# a,b,s,n=0,1,0,int(input())
# while b<=n:
#     a,b,s=b,a+b,s+(b+1)%2*(b)
# print(s)