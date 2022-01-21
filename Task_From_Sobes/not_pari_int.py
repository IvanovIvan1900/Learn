from typing import List
from task_library import *

list_of_data = []
list_of_data.append({'param_input':{'list_in':[7]}, 'return_value':7})
list_of_data.append({'param_input':{'list_in':[0, 1, 0]}, 'return_value':1})
list_of_data.append({'param_input':{'list_in':[0, 1, 0, 1, 0]}, 'return_value':0})

@check_function(data_check=list_of_data)
def solution_my(list_in: List[int]) -> int:
    dic_of_count = {}
    for elem in list_in:
        dic_of_count[elem] = dic_of_count.get(elem, 0) + 1

    iter = (key for key, value in dic_of_count.items() if value %2)
    return next(iter)

if __name__ == "__main__":
    solution_my([])