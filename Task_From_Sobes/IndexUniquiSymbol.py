import array

def unique_char(string):
    counter = 0
    while counter < len(string):
        if not string.count(string[counter]) -1:
            return counter
        counter += 1
    return -1
# мое решение, не оптимально
# def unique_char(input_string: int):
#     dic_of_count = dict((k, input_string.count(k)) for k in input_string )
#     first_sym = -1
#     for sym in input_string:
#         if dic_of_count[sym] == 1:
#             first_sym = input_string.index(sym)
#             break
#
#     return first_sym

if __name__ == '__main__':
    assert unique_char('python')  == 0
    assert unique_char('pythonTop') == 1
    assert unique_char('aabb') == -1
