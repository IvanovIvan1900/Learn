from task_library import *
from random import randint

list_of_data = []
list_of_data.append({'param_input':{'array_in':[1, 6, 3, 2]}, 'return_value':9})
list_of_data.append({'param_input':{'array_in':[1, 2, 3]}, 'return_value':0})
list_of_data.append({'param_input':{'array_in':[4, 5, 3, 2, 0]}, 'return_value':1})
# list_of_data.append({'param_input':{'array_in':}, 'return_value':})
test_data = {"array_in": []}
count_test = 1000

@test_speed(data_in = test_data, iter = count_test)
# @check_function(data_check = list_of_data)
def sum_miss_my(array_in:list) -> int:
    min_in = min(array_in)
    max_in = max(array_in)
    set_in = set(array_in)
    set_full = set(x for x in range(min_in, max_in) )
    
    return sum(set_full-set_in)

@test_speed(data_in = test_data, iter = count_test)
# @check_function(data_check = list_of_data)
def sum_miss_solution(array_in:list) -> int:
    return sum([x for x in range(min(array_in), max(array_in)) if x not in array_in ])

def test_speed_generate_data(count_elem:int):
    global test_data
    test_data["array_in"] = [randint(1, count_elem*2) for _ in range(count_elem)]
    
if __name__ == '__main__':
    test_speed_generate_data(1000)
    sum_miss_my([])
    sum_miss_solution([])