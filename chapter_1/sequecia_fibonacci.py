from functools import lru_cache
from typing import Dict


def fib1(n:int) -> int:
    return fib1(n-1) + fib1(n-2)


def fib2(n:int) -> int:
    if n <= 2:
        return n
    return fib2(n - 1) + fib2(n -2)


memo: Dict[int, int] = {0: 0, 1: 1}


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 1) + fib4(n -2)


def fib5(n: int) -> int:
    if n == 0:
        return n
    last = 0
    next = 1

    for _ in range(1, n):
        last, next = next, last + next # escrevendo dessa maneira, next recebe o seu prórpio valor mais a soma do lest
    return next


def fib6(n):
    yield 0
    if n > 0:
        yield 1
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == '__main__':
    for i in fib6(50):
        print(i)