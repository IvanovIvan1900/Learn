import timeit

def format_phone(phone: str) -> str:
    return "({}) {} {}".format(phone[0:3], phone[3:6], phone[6:])

def format_phone_int(s):
    s_int = int(s)
    a = s_int//10000000
    s_int -= a*10000000

    return f'({a:03}) {s_int//10000:03} {s_int%10000:04}'

def format_phone_solution(s:str) -> str:
    return '({}{}{}) {}{}{} {}{}{}{}'.format(*list(s))

def comapre_function():
    count = 1000000
    time = timeit.timeit(stmt="format_phone('1234567890')",globals=globals(),  number  = count)
    time_int = timeit.timeit(stmt="format_phone_int('1234567890')",globals=globals(),  number  = count)
    time_solution = timeit.timeit(stmt="format_phone_solution('1234567890')",globals=globals(),  number  = count)
    print('Time int is {:.10f}'.format(time_int))
    print('Time     is {:.10f}'.format(time))
    print('Time sol is {:.10f}'.format(time_solution))
    print('{:f}'.format(time_solution/time))

if __name__ == '__main__':
    comapre_function()
    # assert format_phone('0000000000') == '(000) 000 0000'
    # assert format_phone('8005553535') == '(800) 555 3535'
    # assert format_phone('1234567890') ==  '(123) 456 7890'