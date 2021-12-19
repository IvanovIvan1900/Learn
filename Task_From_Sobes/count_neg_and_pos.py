from task_library import *
from typing import List, Tuple
import random

list_of_data = []
list_of_data.append({'param_input':{'array_in':[5, 4, 1, 2, -1, -2]}, 'return_value':(4, 2)})
list_of_data.append({'param_input':{'array_in':[1, 0, -1]}, 'return_value':(1, 1)})
list_of_data.append({'param_input':{'array_in':[0, 0, 0, 0]}, 'return_value':(0,0)})

test_data = {"array_in": []}
test_count = 10


@test_speed(data_in=test_data, iter=test_count)
# @check_function(data_check = list_of_data)
def count_solution(array_in: List[int]) -> Tuple[int, int]:
    pos = sum(1 for x in array_in if x > 0)
    neg = sum(1 for x in array_in if x < 0)
    
    return pos, neg

@test_speed(data_in=test_data, iter=test_count)
def count_yavdoch(array_in: List[int]) -> Tuple[int, int]:
    result = {0: 0, 1: 0}
    [result.update({x<0: result[x<0]+1}) for x in array_in if x !=0]
    return tuple(result.values())

@test_speed(data_in=test_data, iter=test_count)
# @check_function(data_check = list_of_data)
def count_my(array_in: List[int]) -> Tuple[int, int]:
    neg = 0
    pos = 0
    for elem in array_in:
        if elem < 0:
            neg += 1
        elif elem > 0:
            pos += 1
    
    return pos, neg

def generate_test_data(count:int) -> None:
    test_data['array_in'] = [random.randint(-1000, 1000) for _ in range(count)]

if __name__ == "__main__":
    generate_test_data(10000)
    count_solution([])
    count_my([])
    count_yavdoch([])
