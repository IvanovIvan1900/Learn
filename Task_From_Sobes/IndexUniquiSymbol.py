import timeit
from collections import Counter

# def unique_char(s: str):
#     patStr = [i for i in s if s.count(i) == 1]
#     if len(patStr) == 0: return - 1
#     result = s.find(patStr[0])
#     return result

# def unique_char(input_str: str):
#     find = input_str
#     for symb in input_str[len(dict.fromkeys(input_str)):]:
#         find = find.replace(symb, '')
#     return (input_str.index(find[0]) if find else -1)

# def unique_char(string):
#     counter = 0
#     while counter < len(string):
#         if not string.count(string[counter]) -1:
#             return counter
#         counter += 1
#     return -1
def uq_vv(s: str):
    for i, c in enumerate(s):
        if s.count(c) == 1:
            return i
    return -1

def unique_char_kto_to_tam(input_str: str):
    find = input_str
    for symb in find.replace(''.join(dict.fromkeys(find)), ''):
        input_str = input_str.replace(symb, '')
    return (find.index(input_str[0]) if any(input_str) else -1)

# мое решение, не оптимально
def unique_char_my(input_string: int):
    set_of_count = set((k) for k in set(input_string) if input_string.count(k) == 1)
    min_index = -1
    for sym in input_string:
        if sym in set_of_count:
            min_index = input_string.index(sym)
            break

    return min_index

def unique_char_solution(s:str) -> int:
    s = s.lower()
    count = Counter(s)
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx
    return -1

def test_function_on_data(func):
    time_start = timeit.default_timer()
    assert func('python')  == 0
    assert func('pythonTop') == 1
    assert func('aabb') == -1
    assert func('aaabb') == -1
    time_run = (timeit.default_timer() - time_start)
    print('Func is "{}" time is {:f}"'.format(func.__name__, time_run))



if __name__ == '__main__':
    test_function_on_data(unique_char_my)
    test_function_on_data(unique_char_kto_to_tam)
    test_function_on_data(uq_vv)
    test_function_on_data(unique_char_solution)
