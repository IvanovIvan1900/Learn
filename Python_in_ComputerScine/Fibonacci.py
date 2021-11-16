import timeit
from functools import lru_cache



def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)

@lru_cache(maxsize=None)
def fib2_memory(n: int) -> int:
    if n < 2:
        return n
    return fib2_memory(n-1) + fib2_memory(n-2)


dic_of_memory = {0:0, 1:1}

def fib3(n:int) -> int:
    global dic_of_memory
    if n in dic_of_memory:
        return dic_of_memory[n]
    else:
        dic_of_memory[n] = fib3(n - 1) + fib3(n - 2)
        return dic_of_memory[n]

def fib4(n:int) -> int:
    rez = 0
    if n < 2:
        return n
    last, next,  = 0 , 1
    for i in range(1, n):
        rez = last + next
        last, next = next , next+last

    return rez

def test_function_on_data(func, n):
    time_start = timeit.default_timer()
    print(func(n))
    time_run = (timeit.default_timer() - time_start)
    print('Func is "{}" time is {:f}"'.format(func.__name__, time_run))

if __name__ == '__main__':
    n = 15
    test_function_on_data(fib2, n)
    test_function_on_data(fib3, n)
    test_function_on_data(fib2_memory, n)
    test_function_on_data(fib4, n)
