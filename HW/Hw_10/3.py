from time import time
from functools import cache


def process_timer(func):
    def test_time(*args, **kwargs):
        start_of_time = time()
        res = func(*args, **kwargs)
        end_of_time = time()
        print(f"Test Time is : {end_of_time - start_of_time}")
        return res

    return test_time


def recur_fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return recur_fibonacci(num - 1) + recur_fibonacci(num - 2)


@process_timer
@cache
def fib(num):
    for i in range(num):
        recur_fibonacci(num)


def recur_factorial(num):
    if num == 1:
        return num
    else:
        return num * recur_factorial(num - 1)


@process_timer
@cache
def fact(num):
    for i in range(num):
        recur_factorial(num)


fib(25)
fact(900)
